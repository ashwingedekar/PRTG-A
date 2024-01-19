import requests
import xml.etree.ElementTree as ET

# PRTG API endpoint for reading Syslog messages
api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=messages&columns=objid,datetime,type,name,status,messageid,message&filter_drel=100days&id=3022&username=Ashwin.Gedekar&passhash=3422185132'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse XML response
    root = ET.fromstring(response.text)

    # Loop through each item and print messages
    for item in root.findall('.//item'):
        objid = item.find('objid').text
        datetime = item.find('datetime').text
        message_type = item.find('type').text
        name = item.find('name').text
        status = item.find('status').text

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
