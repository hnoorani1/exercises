import xml.etree.ElementTree as ET
from datetime import timedelta, date

"""Create a python method that takes arguments int X and int Y,
and updates DEPART and RETURN fields
in test_payload.xml:

- DEPART gets set to X days in the future from the current date
(whatever the current date is at the moment of executing the code)
- RETURN gets set to Y days in the future from the current date

Please write the modified XML to a new file."""

def update_depart_return_fields (depart_date,return_date):
	"""
	Takes argument dates, adds a few days in the future and ouputs a new XML 
	:param depart_date: This is the depart date in the future
	:param return_date: This is the return date in the future
	"""

depart_date = (date.today() + timedelta(days=10))
return_date = (date.today() + timedelta(days=15))

tree = ET.parse('test_payload.xml')
root = tree.getroot()

for TP in root.iter('DEPART'):
	TP.text = str(depart_date)

for TP in root.iter('RETURN'):
	TP.text = str(return_date)
tree.write('updated_depart_return_fields.xml')