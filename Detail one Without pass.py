#import requests
#response = requests.get("https://jp-vivekp-40-58.comtelindia.com/api/table.xml?content=sensors&columns=sensor&apitoken=4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======")
#print(response)


import requests

api_endpoint = 'https://jp-vivekp-40-58.comtelindia.com/api/getsensordetails.json?id=10359'
api_token = '4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======'

# Define parameters for the API call
params = {
    'content': 'sensortree',
    'apitoken': api_token,
}

# Make the API request
response = requests.get(api_endpoint, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")
