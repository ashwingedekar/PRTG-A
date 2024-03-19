import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML data
tree = ET.parse("prtg-101.100.xml")
root = tree.getroot()

# Define a function to extract data from XML nodes
def extract_data(node):
    data = {}
    for child in node:
        if child.tag == "name":
            data["Name"] = child.text
        elif child.tag == "id":
            data["ID"] = child.text
        elif child.tag == "status":
            data["Status"] = child.text
    return data

# Extract data from XML and store it in a list of dictionaries
sensor_data = []
for sensor_node in root.findall(".//sensor"):
    sensor_data.append(extract_data(sensor_node))

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(sensor_data)

# Write the DataFrame to an Excel file
df.to_excel("zzzz.xlsx", index=False)
