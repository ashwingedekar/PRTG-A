#import requests
#response = requests.get("https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&columns=sensor&apitoken=GJMJ23FVPUXRS4Q4PGZUR4EZXA4DUQDPJ5F3KDFEQY======")
#print(response)


#/api/getobjectproperty.htm?id=objectid&name=propertyname&show=nohtmlencode



#api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml'

#
import requests

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.xml?id=3007&avg=60&sdate=2024-01-10-15-00-00&edate=2024-01-10-16-00-00'
api_token = '7W3Y4SO3EXLMPGU3TGP5H3W46FFWCY2UJJBQ3HU7PA======'

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
    print(response.text)
    # Save the response to an XML file
    file_path = 'c:/prtg/response.xml'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f"Response saved to: {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")



