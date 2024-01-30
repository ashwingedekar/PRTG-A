import requests
import xml.etree.ElementTree as ET

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=device&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")

    # Parse the XML response
    root = ET.fromstring(response.content)

    # Prepare HTML table data
    table_data = "<table border='1'><tr><th>Group</th><th>Device</th><th>Status</th></tr>"

    # Iterate through each item element and generate table rows
    for item in root.findall('item'):
        group_element = item.find('group')
        if group_element is not None and group_element.text:
            group = group_element.text
            device_element = item.find('device')
            device = device_element.text if device_element is not None and device_element.text else "N/A"
            status_element = item.find('status')
            status = status_element.text if status_element is not None and status_element.text else "N/A"
            table_data += f"<tr><td>{group}</td><td>{device}</td><td>{status}</td></tr>"

    table_data += "</table>"

    # Save the XML data to a file
    file_path = "C:/prtg/output.html"
    with open(file_path, "wb") as file:
        file.write(table_data.encode())

    print(f"HTML table data saved to {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")
