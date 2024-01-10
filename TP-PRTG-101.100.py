#import requests
#response = requests.get("https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&columns=sensor&apitoken=GJMJ23FVPUXRS4Q4PGZUR4EZXA4DUQDPJ5F3KDFEQY======")
#print(response)


#/api/getobjectproperty.htm?id=objectid&name=propertyname&show=nohtmlencode

import requests

#api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml'

#


api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443//api/getobjectstatus.htm?id=10359&name=message'

api_token = 'GJMJ23FVPUXRS4Q4PGZUR4EZXA4DUQDPJ5F3KDFEQY======'

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
