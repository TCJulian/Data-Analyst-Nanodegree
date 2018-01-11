import collections
import json
import re

def audit_phone_nums(element, tag)
    def audit():
        for tags in element['node']:
            if tags['key'] == 'phone':
                old_value = tags['value']
                new_value = phone(old_value)
                if old_value == new_value:
                    continue
                elif new_value == "***Unknown format. No changes made.***":
                    changelist.append([old_value, new_value])
                else:
                    tags['value'] = new_value
                    changelist.append([old_value, new_value])
        return element
        
    def check_phone(num):
        if not correct_re.search(num):
            num = num.replace("(", "")
            num = num.replace(")", "")
            num = num.replace("+", "")
            num = num.replace(" ", "")
            if not correct_re.search(num):
                num = "***Unknown format. No changes made.***"
                return num
        return num
           
    correct_re = re.compile(r'1?\d{10}$')
        
    changelist = []
    
    if tag == 'node'
        element = audit()
        
    # Writes the changes to a text file and returns audited element.
    with open("phone_changelist.txt", "a") as file:
        if len(changelist) > 0:
            file.write(json.dumps(changelist) + "\n")
    return element
