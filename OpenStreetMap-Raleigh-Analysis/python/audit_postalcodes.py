import collections
import json
import re

def audit_postcodes(element, tag):
    # Internal function that searches for postcode tags and performs an audit.
    def audit(tag_type):
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

    # re formats check for dashes and any characters besides numbers.
    postal_re_zip4 = re.compile('[-]')
    postal_re_char = re.compile('[^0-9]')

    # Lists to store any changes made to the original data.
    bad_zip4 = []
    bad_char = []
    unknown = []

    if tag == "node":
        element = audit("node_tags")
    elif tag == "way":
        element = audit("way_tags")

    # Writes the changes to a text file and returns audited element.
    with open("postcode_changelist.txt", "a") as file:
        auditted_codes = {"Zip+4":bad_zip4, "Characters":bad_char, "Unknown":unknown}
        for key, value in auditted_codes.items():
            if len(value) > 0:
                file.write(key + ":" + json.dumps(value) + "\n")
    return element
