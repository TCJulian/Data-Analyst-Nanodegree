import re
from json import dumps

def audit_postalcodes(element, tag):
    """Audits postal codes, writes changelist to file, and returns an updated element.

    Keyword arguments:
    element -- A shaped element, created by `osm_to_cvs` script
    tag -- The tag type (`node` or `way`) as a string
    """
    
    def audit(tag_type):
        """Checks each `postcode` tag value, updates value in shaped element, and adds changes to changelist."""
        for tags in element[tag_type]:
            if tags['type'] == 'addr' and tags['key'] == 'postcode':
                old_value = tags['value']
                if postal_re_zip4.search(old_value):
                    new_value = old_value[:5]
                    tags['value'] = new_value
                    changelist.append([old_value, new_value])
                elif postal_re_char.search(old_value):
                    new_value = re.sub('[a-z]', '', old_value,  flags=re.IGNORECASE)
                    tags['value'] = new_value
                    changelist.append([old_value, new_value])
                elif len(old_value) != 5:
                    new_value = "***Unknown format. No changes made.***"
                    changelist.append([old_value, new_value])
        return element

    postal_re_zip4 = re.compile('[-]')
    postal_re_char = re.compile('[^0-9]')

    changelist = []

    if tag == "node":
        element = audit("node_tags")
    elif tag == "way":
        element = audit("way_tags")

    # Writes the changes to a text file and returns audited element.
    with open("changelist_postcode.txt", "a") as file:
        if len(changelist) > 0:
            file.write(dumps(changelist) + "\n")
    return element
