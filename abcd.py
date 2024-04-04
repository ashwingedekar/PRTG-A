import csv
import xml.etree.ElementTree as ET

# Path to your XML file
xml_file_path = "101.100sensorsnmptable.xml"

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Extract objid elements
objid_list = []

# Loop through all item elements and extract objid
for item in root.findall('.//item'):
    objid_element = item.find('objid')
    if objid_element is not None:
        objid = objid_element.text
        objid_list.append(objid)

# Path to save the CSV file
csv_file_path = "abcdef.csv"

# Write objid values to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["objid"])  # Write header
    for objid in objid_list:
        writer.writerow([objid])
