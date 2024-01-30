import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import os

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=devices&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")

    # Parse the XML response
    root = ET.fromstring(response.content)

    # Prepare XML data
    xml_data = ET.Element('data')
    
    # Iterate through each item element and add it to XML data
    for item in root.findall('item'):
        group_element = item.find('group')
        if group_element is not None and group_element.text:
            group = group_element.text
            device_element = item.find('device')
            device = device_element.text if device_element is not None and device_element.text else "N/A"
            status_element = item.find('status')
            status = status_element.text if status_element is not None and status_element.text else "N/A"
            
            # Create an item element and add group, device, and status as sub-elements
            item_element = ET.SubElement(xml_data, 'item')
            group_sub_element = ET.SubElement(item_element, 'group')
            group_sub_element.text = group
            device_sub_element = ET.SubElement(item_element, 'device')
            device_sub_element.text = device
            status_sub_element = ET.SubElement(item_element, 'status')
            status_sub_element.text = status

    # Convert XML data to string
    xml_string = ET.tostring(xml_data, encoding='unicode')

    # Create directory if it doesn't exist
    directory = "C:/prtg"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the XML data to a file with current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_path = f"{directory}/output_{current_datetime}.xml"
    with open(file_path, "w") as file:
        file.write(xml_string)

    print(f"XML data saved to {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")
