import csv
import requests

# Read ID values from the file
id_values = {}
with open("sensor_id.txt", "r") as file:
    for line in file:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=")
            id_values[key] = value

# API endpoint template
api_endpoint_template = 'https://qnq-99-51.comtelindia.com:10443/api/getsensordetails.json?id={}&username=prtgadmin&passhash=378387200'

# Create a list to store sensor ID and parent device name
data = []

# Iterate over each ID to make API requests
for key, id_value in id_values.items():
    # Construct the API endpoint URL using the ID value
    api_endpoint = api_endpoint_template.format(id_value)
    
    # Make the API request
    response = requests.get(api_endpoint)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        json_response = response.json()
        # Extract the value of the "parentdevicename" field
        parent_device_name = json_response["sensordata"]["parentdevicename"]
        # Append ID value and corresponding device name to the data list
        data.append((id_value, parent_device_name))
        print(f"Parent Device Name for {id_value}: {parent_device_name}")
    else:
        print(f"Error for {id_value}: {response.status_code} - {response.text}")

# Write the data to a CSV file
with open("sensor_parent_device.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write header row
    csv_writer.writerow(["Sensor ID", "Parent Device Name"])
    # Write data rows
    csv_writer.writerows(data)

print("CSV file created successfully.")
