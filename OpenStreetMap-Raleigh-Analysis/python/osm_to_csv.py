#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET

import cerberus

import schema
import audit_postalcodes
import audit_street_names

OSM_PATH = "raleigh_north-carolina.osm"

NODES_PATH = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH = "ways_tags.csv"

LOWER_COLON = re.compile(r'^([a-z]|_)+:([a-z]|_)+')
PROBLEMCHARS = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

SCHEMA = schema.schema

# The fields in the csvs MUST match the column order in the sql table schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']


def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS, 
                  lower_colon=LOWER_COLON, problem_chars=PROBLEMCHARS, default_tag_type='regular'):
    """Clean and shape node or way XML element to Python dict"""

    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements

    # Begin collecting first level node attributes
    if element.tag == 'node':
        try:
            for tag in node_attr_fields:
                node_attribs[tag] = element.attrib[tag]
        except ValueError:
            print("Couldn't find \"{}\" attribute in \"node\" tag.".format(tag))
            raise()
            
        # Collect second level node tag attributes
        for sec_tag in element.iter("tag"):
            tag_attribs = {}
            if problem_chars.search(sec_tag.attrib["k"]):
                continue
            elif lower_colon.search(sec_tag.attrib["k"]):
                split_sec_tag = sec_tag.attrib["k"].split(":", 1)
                tag_attribs["type"] = split_sec_tag[0]
                tag_attribs["key"] = split_sec_tag[1]
            else:
                tag_attribs["type"] = default_tag_type
                tag_attribs["key"] = sec_tag.attrib["k"]
            tag_attribs["id"] = node_attribs["id"]
            tag_attribs["value"] =sec_tag.attrib["v"]
            tags.append(tag_attribs)
        return {'node': node_attribs, 'node_tags': tags}
     
    # Begin collecting first level way attributes.
    elif element.tag == 'way':
        position = 0
        try:
            for tag in WAY_FIELDS:
                way_attribs[tag] = element.attrib[tag]
        except ValueError:
            print("Couldn't find \"{}\" attribute in \"way\" tag.".format(tag))
            raise()
        
        # Collect second level way node attribs and position.
        for nd in element.iter("nd"):
            nd_dic = {}
            nd_dic["id"] = way_attribs["id"]
            nd_dic["node_id"] = nd.attrib["ref"]
            nd_dic["position"] = position
            position += 1
            way_nodes.append(nd_dic)
            
        # Collect second level way tag attributes
        for tag in element.iter("tag"):
            if tag.tag == "tag":
                tag_attribs = {}
                if PROBLEMCHARS.search(tag.attrib["k"]):
                    continue
                elif LOWER_COLON.search(tag.attrib["k"]):
                    split_tag = tag.attrib["k"].split(":", 1)
                    tag_attribs["type"] = split_tag[0]
                    tag_attribs["key"] = split_tag[1]
                else:
                    tag_attribs["type"] = "regular"
                    tag_attribs["key"] = tag.attrib["k"]
                tag_attribs["id"] = way_attribs["id"]
                tag_attribs["value"] =tag.attrib["v"]
                tags.append(tag_attribs)
        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}


# ================================================== #
#               Helper Functions                     #
# ================================================== #

# The following helper functions were provided by the Udacity Data Analyst Nanodegree program.
# I did not write the following code.

def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()


def validate_element(element, validator, schema=SCHEMA):
    """Raise ValidationError if element does not match schema"""
    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)
        
        raise Exception(message_string.format(field, error_string))


class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
            k: (v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in row.iteritems()
        })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)

# ================================================== #
#               Main Function                        #
# ================================================== #

# The majority of the following function was created by the 
# Udacity Data Analyst Nanodegree program. Auditing functions 
# created by myself are commented accordingly.

def process_map(file_in, validate):
    """Iteratively process each XML element and write to csv(s)"""

    with codecs.open(NODES_PATH, 'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH, 'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH, 'w') as way_tags_file:

        nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
        way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        validator = cerberus.Validator()

        for element in get_element(file_in, tags=('node', 'way')):
            el = shape_element(element)
            if el:
                # Audit functions below were created by myself.
                el = audit_postalcodes.audit_postcodes(el, element.tag)
                el = audit_street_names.audit_streetnames(el, element.tag)
                
                if validate is True:
                    validate_element(el, validator)

                if element.tag == 'node':
                    nodes_writer.writerow(el['node'])
                    node_tags_writer.writerows(el['node_tags'])
                elif element.tag == 'way':
                    ways_writer.writerow(el['way'])
                    way_nodes_writer.writerows(el['way_nodes'])
                    way_tags_writer.writerows(el['way_tags'])


if __name__ == '__main__':
    # Note: Validation is ~ 10X slower. For large project, consider using a small
    # sample of the map when validating.
    process_map(OSM_PATH, validate=False)
