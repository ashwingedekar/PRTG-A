import requests
import xml.etree.ElementTree as ET

# PRTG API endpoint for reading Syslog messages
api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=messages&columns=objid,message&id=3022&username=Ashwin.Gedekar&passhash=3422185132'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse XML response
    root = ET.fromstring(response.text)

    # Loop through each item and print messages
    for item in root.findall('.//item'):
        objid = item.find('objid').text

        # Check if 'datetime' element exists
        datetime_element = item.find('datetime')
        datetime = datetime_element.text if datetime_element is not None else None

        message_type_element = item.find('type')
        message_type = message_type_element.text if message_type_element is not None else None

        name_element = item.find('name')
        name = name_element.text if name_element is not None else None

        status_element = item.find('status')
        status = status_element.text if status_element is not None else None

        # Check if 'messageid' element exists
        message_id_element = item.find('messageid')
        message_id = message_id_element.text if message_id_element is not None else None

        message_element = item.find('message')
        message = message_element.text if message_element is not None else None

        print(f"\nObject ID: {objid}")
        print(f"Date and Time: {datetime}")
        print(f"Message Type: {message_type}")
        print(f"Name: {name}")
        print(f"Status: {status}")
        print(f"Message ID: {message_id}")
        print(f"Message: {message}")

else:
    print(f"Error: {response.status_code} - {response.text}")
