import csv
import requests
from tqdm import tqdm
from xml.etree import ElementTree as ET

# Read ID values from the file
id_values = {}
with open("sensor_id.txt", "r") as file:
    for idx, line in enumerate(file, start=1):
        line = line.strip()
        if "=" in line:
            key, value = line.split("=")
            id_values[key] = value

# API endpoint template
api_endpoint_template = 'https://qnq-99-51.comtelindia.com:10443/api/table.xml?content=sensortree&username=prtgadmin&passhash=378387200'

# Create a list to store the data
data = []

# Iterate over each ID to make API requests
progress_bar = tqdm(total=len(id_values), desc="Fetching limits for each ID")
for key, id_value in id_values.items():
    # Construct the API endpoint URL using the ID value
    api_endpoint = api_endpoint_template.format(id_value)
    
    # Make the API request
    response = requests.get(api_endpoint)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the XML response
        xml_response = ET.fromstring(response.content)
        # Extract the value of the "parentdevicename" field
        parent_device_name = xml_response.find(".//parentdevicename").text
        # Append ID value and corresponding device name to the data list
        data.append((id_value, parent_device_name))
    else:
        print(f"Error for {key}: {response.status_code} - {response.text}")
    progress_bar.update(1)

progress_bar.close()

# Write the data to a CSV file
with open("99_51.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header row
    csv_writer.writerow(["ID", "Device Name"])
    # Write data rows
    csv_writer.writerows(data)

print("Output written to 99_51.csv")
