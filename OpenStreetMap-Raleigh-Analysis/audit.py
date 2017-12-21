import json
import re

def audit_postcodes(element, tag):
    postal_re_zip4 = re.compile('[-]')
    postal_re_char = re.compile('[^0-9]')

    bad_zip4 = []
    bad_char = []
    unknown = []
    auditted_codes = {"Zip+4":bad_zip4, "Characters":bad_char, "Unknown":unknown}

    if tag == "node":
        if element['node_tags']['type'] == 'addr' and element['node_tags']['key'] == 'postcode':
            old_value = element['node_tags']['value']
            if postal_re_zip4.search(old_value):
                new_value = old_value[:5]
                element['node_tags']['value'] = new_value
                bad_zip4.append([old_value, new_value])
            elif postal_re_char.search(old_value):
                new_value = old_value
                re.sub('[a-z]', '', re.IGNORECASE, new_value)
                element['node_tags']['value'] = new_value
                bad_char.append([old_value, new_value])
            elif len(old_value) != 5:
                unknown.append([old_value, "Error. Can't handle this exception."])
        
    elif tag == "way":
        pass
    
    with open("changelist.txt", "w) as file:
        file.write(json.dumps(auditted_codes))
        
    return element
