import pandas as pd
import json
import requests

# API endpoint
api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/getsensordetails.json?id=3022&username=Ashwin.Gedekar&passhash=3422185132'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Load JSON response
    data = json.loads(response.text)

    # Convert to DataFrame (table)
    df = pd.json_normalize(data)

    # Save DataFrame to CSV file in C:/prtg directory
    file_path = 'C:/prtg/output.csv'
    df.to_csv(file_path, index=False)

    print(f"DataFrame saved to {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")
