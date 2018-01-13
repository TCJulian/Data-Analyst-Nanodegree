from json import dumps
import re

def audit_phone_nums(element, tag):
    """Audits phone number, writes changelist to file, and returns an updated element.

    Keyword arguments:
    element -- A shaped element, created by `osm_to_cvs` script
    tag -- The tag type (`node` or `way`) as a string
    """
    def audit():
        """Checks each `phone` tag value, updates value in shaped element, and adds changes to changelist."""
        for tags in element['node_tags']:
            if tags['key'] == 'phone':
                old_value = tags['value']
                new_value = check_phone(old_value)
                if old_value == new_value:
                    continue
                elif new_value == "***Unknown format. No changes made.***":
                    changelist.append([old_value, new_value])
                else:
                    tags['value'] = new_value
                    changelist.append([old_value, new_value])
        return element

    def check_phone(num):
        """Returns phone number with all non-digit characters removed."""
        if not correct_re.search(num):
            num = re.sub(r'\D', '', num)
            if not correct_re.search(num):
                num = "***Unknown format. No changes made.***"
                return num
        return num

    correct_re = re.compile(r'1?\d{10}$')

    changelist = []

    if tag == 'node':
        element = audit()

    # Writes the changes to a text file and returns audited element.
    with open("changelist_phone.txt", "a") as file:
        if len(changelist) > 0:
            file.write(dumps(changelist) + "\n")
    return element
