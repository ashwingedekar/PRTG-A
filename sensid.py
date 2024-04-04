import xml.etree.ElementTree as ET
import csv

# Path to the XML file
xml_file = '101.100sensorsnmptable.xml'

# Parse XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Open CSV file for writing
with open('101.100_SNMP.csv', 'w', newline='') as csvfile:
    fieldnames = ['objid']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write header
    writer.writeheader()

    # Iterate over <item> elements
    for item in root.findall('.//item'):
        # Find the objid element
        objid_element = item.find('objid')
        
        # Check if objid element exists
        if objid_element is not None:
            objid = objid_element.text
            # Write data to CSV
            writer.writerow({'objid': objid})
        else:
            print("objid element not found in the item.")
