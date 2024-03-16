import requests

# Read ID values from the file
id_values = {}
with open("sensor_id.txt", "r") as file:
    for idx, line in enumerate(file, start=1):
        line = line.strip()
        if "=" in line:
            key, value = line.split("=")
            id_values[key] = value

# API endpoint template
api_endpoint_template = 'https://tp-prtg-101-100.comtelindia.com:10443/api/getsensordetails.json?id={}&username=Ashwin.Gedekar&passhash=1132296586'

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
        # Print ID value and corresponding device name
        print(f" {parent_device_name}")
    else:
        print(f"Error for {key}: {response.status_code} - {response.text}")
