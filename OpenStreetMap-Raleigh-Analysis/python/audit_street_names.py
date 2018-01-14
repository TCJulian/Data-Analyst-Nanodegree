import re
from json import dumps

def audit_street_names(element, tag):
    """Audits street names, writes changelist to file, and returns an updated element.

    Keyword arguments:
    element -- A shaped element, created by `osm_to_cvs` script
    tag -- The tag type (`node` or `way`) as a string
    """

    def audit(tag_type):
        """Checks each `street` tag value, updates value in shaped element, and adds changes to changelist."""
        for tags in element[tag_type]:
            if tags['type'] == 'addr' and tags['key'] == 'street':
                old_value = tags['value']
                new_value = audit_street_type(old_value)
                if old_value == new_value:
                    continue
                elif new_value == "***Unknown Mapping. No changes made.***":
                    changelist.append([old_value, new_value])
                else:
                    tags['value'] = new_value
                    changelist.append([old_value, new_value])
        return element

    def audit_street_type(street_name):
        """Searches `street_name` for a pattern and compares pattern against list of expected values, returning an updated street name if not in expected.
        """
        m = street_type_re.search(street_name)
        if m:
            street_type = m.group()
            if street_type not in expected:
                new_name = update_name(street_name, mapping)
                return new_name
        return street_name

    def update_name(name, mapping):
        """Searches `name` for a series of keys from dict `mapping`, replacing `name` with the key-value if match is found."""
        for map in mapping:
            mapping_re = r'\s' + re.escape(map) + r'(\s|$)'
            if re.search(mapping_re, name, re.IGNORECASE):
                new_name = name.replace(map, mapping[map])
                return new_name
        # passes street name ending with digits if name falls through loop
        if street_digits_re.search(name):
            return name
        else:
            reply = "***Unknown Mapping. No changes made.***"
            return reply
    
    street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
    street_digits_re = re.compile(r'\d+$')

    expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Trail", "Parkway", "Commons", "Circle", "Way", "Parkway", "Highway", "Loop", "Run", "Crossing", "North", "South", "East", "West", "Plaza", "Extension", "Crescent", "Fork", "Bypass", "Ridge", "Hall", "Hill", "Terrace", "Point", "Alley", "Grove"]

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
                "Pky": "Parkway",
                "Pkwy": "Parkway"
                }

    changelist = []

    if tag == "node":
        element = audit("node_tags")
    elif tag == "way":
        element = audit("way_tags")

    # Writes the changes to a text file and returns audited element.
    with open("changelist_streetname.txt", "a") as file:
        if len(changelist) > 0:
            file.write(dumps(changelist) + "\n")
    return element
