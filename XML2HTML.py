import xml.etree.ElementTree as ET

# Specify the file path where your XML data is stored
xml_file_path = "C:/prtg/SYSLOG.xml"

# Read XML data from the file
try:
    with open(xml_file_path, "r") as xml_file:
        xml_data = xml_file.read()
except FileNotFoundError:
    print(f"Error: The file '{xml_file_path}' does not exist.")
    exit()

# Parse XML data
root = ET.fromstring(xml_data)

# Extract data from XML and create HTML table
html_table = """
<table border="1">
    <tr>
        <th>Attribute</th>
        <th>Value</th>
    </tr>
"""

for element in root:
    attribute = element.tag
    value = element.text.strip() if element.text else ""
    html_table += f"    <tr><td>{attribute}</td><td>{value}</td></tr>\n"

html_table += "</table>"

# Save the HTML table to a file
html_file_path = "C:/prtg/output_table.html"
with open(html_file_path, "w") as html_file:
    html_file.write(html_table)

print(f"HTML table saved to {html_file_path}")
