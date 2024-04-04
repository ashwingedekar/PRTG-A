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

# Iterate over each ID to make API requests
for key, id_value in id_values.items():
    # Construct the API endpoint URL using the ID value
    api_endpoint = api_endpoint_template.format(id_value)
    
    # Make the API request
    response = requests.get(api_endpoint)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(f"Request successful for {key}!")
        print("Response:")
        print(response.text)
        
        # If you want to save the response to a file, uncomment the following lines
        # file_path = f"{key}_sensor_details.json"
        # with open(file_path, "w") as file:
        #     file.write(response.text)
        # print(f"Sensor details saved to {file_path}")
    else:
        print(f"Error for {key}: {response.status_code} - {response.text}")
    
    
