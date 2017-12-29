import collections
import json
import re

def audit_postcodes(element, tag):
    # Internal function that searches for postcode tags and performs an audit.
    def check_postcode(tag_type):
        for tags in element[tag_type]:
            if tags['type'] == 'addr' and tags['key'] == 'postcode':
                old_value = tags['value']
                if postal_re_zip4.search(old_value):
                    new_value = old_value[:5]
                    tags['value'] = new_value
                    bad_zip4.append([old_value, new_value])
                elif postal_re_char.search(old_value):
                    new_value = old_value
                    new_value = re.sub('[a-z]', '', new_value,  flags=re.IGNORECASE)
                    tags['value'] = new_value
                    bad_char.append([old_value, new_value])
                elif len(old_value) != 5:
                    new_value = old_value[:5]
                    tags['value'] = new_value
                    unknown.append([old_value, new_value])
        return element

    # re formats used in the function above.
    postal_re_zip4 = re.compile('[-]')
    postal_re_char = re.compile('[^0-9]')

    # Lists to store any changes made to the original data.
    bad_zip4 = []
    bad_char = []
    unknown = []

    if tag == "node":
        element = check_postcode("node_tags")
    elif tag == "way":
        element = check_postcode("way_tags")

    # Writes the changes to a text file and returns audited element.
    with open("changelist.txt", "a") as file:
        auditted_codes = {"Zip+4":bad_zip4, "Characters":bad_char, "Unknown":unknown}
        for key, value in auditted_codes.items():
            if len(value) > 0:
                file.write(key + ":" + json.dumps(value) + "\n")
    return element


def audit_streetnames(element, tag):
    def audit(tag_type):
        for tags in element[tag_type]:
            if tags['type'] == 'addr' and tags['key'] == 'street':
                old_value = tags['value']
                new_value = audit_street_type(old_value)
                changelist.append([old_value, new_value])
        return element

    def audit_street_type(street_name):
        m = street_type_re.search(street_name)
        if m:
            street_type = m.group()
            if street_type not in expected:
                new_name = update_name(street_name, mapping)
                return new_name
        else:
            return street_name


    def update_name(name, mapping):
        for map in mapping:
            if map in name:
                name = name.replace(map, mapping[map])
                return name
        reply = "***Update Mapping***"
        return reply

    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

    expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square",
                "Lane", "Road", "Trail", "Parkway", "Commons", "Circle", "Way", 
                "Parkway", "Highway", "Loop", "Run", "Crossing"]

    mapping = { "St": "Street",
                "St.": "Street",
                "Ave": "Avenue",
                "Rd": "Road",
                "Rd.": "Road",
                "Ct": "Court",
                "Ct.": "Court",
                "Ln": "Lane",
                "Ln.": "Lane",
                "Blvd": "Boulevard",
                "Blvd.": "Boulevard",
                "Dr": "Drive",
                "Dr.": "Drive"
                }

    changelist = []

    if tag == "node":
        element = audit("node_tags")
    elif tag == "way":
        element = audit("way_tags")

    # Writes the changes to a text file and returns audited element.
    with open("streetname_changelist.txt", "a") as file:
        if len(changelist) > 0 and changelist[0][0] != changelist[0][1]:
            file.write(json.dumps(changelist) + "\n")
    return element
