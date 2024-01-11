#import requests
#response = requests.get("https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&columns=sensor&apitoken=GJMJ23FVPUXRS4Q4PGZUR4EZXA4DUQDPJ5F3KDFEQY======")
#print(response)


#/api/getobjectproperty.htm?id=objectid&name=propertyname&show=nohtmlencode



#api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml'

#
import requests

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.json?id=3007&avg=60&sdate=2024-01-10-15-00-00&edate=2024-01-10-16-00-00&usecaption=1 '
api_token = 'JBOARQESZRQTMSNZHTZM4CFMBFWVGNH4NX2OV2OYEU======'

#/api/historicdata.json?id=3007&avg=60&sdate=2024-01-10-15-00-00&edate=2024-01-10-16-00-00&usecaption=1   //  json formate
#api/historicdata.xml?id=3007&avg=60&sdate=2024-01-10-15-00-00&edate=2024-01-10-16-00-00     // xml formate
# Define parameters for the API call
params = {
    
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



