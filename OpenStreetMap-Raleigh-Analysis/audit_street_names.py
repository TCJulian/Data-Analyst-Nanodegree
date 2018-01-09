import collections
import json
import re

def audit_streetnames(element, tag):
    def audit(tag_type):
        for tags in element[tag_type]:
            if tags['type'] == 'addr' and tags['key'] == 'street':
                old_value = tags['value']
                new_value = audit_street_type(old_value)
                if old_value == new_value:
                    continue
                elif new_value == "***Unknown Mapping***":
                    changelist.append([old_value, new_value])
                else:
                    tags['value'] = new_value
                    changelist.append([old_value, new_value])
        return element

    def audit_street_type(street_name):
        m = street_type_re.search(street_name)
        if m:
            street_type = m.group()
            if street_type not in expected:
                new_name = update_name(street_name, mapping)
                return new_name
        return street_name

    def update_name(name, mapping):
        for map in mapping:
            #mapping_re = r'\s{0}\s?\b?'.format(map)
            #if re.search(mapping_re, name, re.IGNORECASE):
            if map in name:
                new_name = name.replace(map, mapping[map])
                return new_name
        if street_digits_re.search(name):
            return name
        else:
            reply = "***Unknown Mapping***"
            return reply

    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
    street_digits_re = re.compile(r'\d+$')

    expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Trail", "Parkway", "Commons", "Circle", "Way", "Parkway", "Highway", "Loop", "Run", "Crossing", "North", "South", "East", "West", "Plaza", "Extension", "Crescent", "Fork"]

    mapping = { "St.": "Street",
                "St": "Street",
                "Ave": "Avenue",
                "Rd.": "Road",
                "Rd": "Road",
                "Ct.": "Court",
                "Ct": "Court",
                "Ln.": "Lane",
                "Ln": "Lane",
                "Blvd.": "Boulevard",
                "Blvd": "Boulevard",
                "Dr.": "Drive",
                "Dr": "Drive",
                "Pl.": "Place",
                "Pl": "Place",
                "Ext.": "Extension",
                "Ext": "Extension",
                "Pky": "Parkway"
                }

    changelist = []

    if tag == "node":
        element = audit("node_tags")
    elif tag == "way":
        element = audit("way_tags")

    # Writes the changes to a text file and returns audited element.
    with open("streetname_changelist.txt", "a") as file:
        if len(changelist) > 0:
            file.write(json.dumps(changelist) + "\n")
    return element
