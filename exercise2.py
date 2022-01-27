import json

"""
2. Create a python method that takes a json element
as an argument, and removes that element from test_payload.json.

Please verify that the method can remove either nested or non-nested elements
(try removing "outParams" and "appdate").

Please write the modified json to a new file.
"""

def removing_json_element(nested, non_nested):
	"""
	Removes certain JSON elements from test_payload.json. Outputs a new json file.
	:param nested: this is the nested element from the json
	:param non_nested: this is the non_nested element from the json
	"""
nested = 'appdate'
non_nested = 'outParams'

with open('test_payload.json', 'r') as data_file:
    data = json.load(data_file)

#Deletes outParams from the JSON
#Deletes nested appdate from the JSON
for element in data:
	del element[non_nested]
	del element['inParams'][nested]

#writes the modified json to a new json file
with open('updated_file.json', 'w') as data_file:
    data = json.dump(data, data_file)
