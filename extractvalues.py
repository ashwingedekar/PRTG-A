import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Define the API endpoint
api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensortree&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    
    # Parse the XML response
    root = ET.fromstring(response.content)
    
    # Initialize lists to store data
    names = []
    ids = []

    # Find all <sensor> elements within <sensortree>
    sensors = root.find('.//sensortree')

    # Iterate over each <sensor> element
    for sensor in sensors.findall('.//sensor'):
        # Attempt to extract data from each <sensor> element
        try:
            name = sensor.find('name').text
            id = sensor.find('id').text

            # Append data to respective lists
            names.append(name)
            ids.append(id)
        except Exception as e:
            print(f"Error extracting data from sensor element: {e}")

    # Create a DataFrame from the extracted data
    if names and ids:
        data = {
            'Name': names,
            'ID': ids
        }
        df = pd.DataFrame(data)

        # Specify the path for the Excel file
        excel_file_path = "C:/prtg/sensornameiddata.xlsx"

        # Save the DataFrame to Excel
        df.to_excel(excel_file_path, index=False)

        print(f"Sensor data saved to {excel_file_path}")
    else:
        print("No sensor data found in the XML response.")
    
else:
    print(f"Error: {response.status_code} - {response.text}")
