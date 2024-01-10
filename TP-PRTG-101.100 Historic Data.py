#import requests
#response = requests.get("https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&columns=sensor&apitoken=GJMJ23FVPUXRS4Q4PGZUR4EZXA4DUQDPJ5F3KDFEQY======")
#print(response)


#/api/getobjectproperty.htm?id=objectid&name=propertyname&show=nohtmlencode



#api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml'

#
import requests

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.xml?id=3007&avg=0&sdate=2024-01-08-00-00-00&edate=2024-01-08-00-00-00' 
#id=10359



api_token = '3P2G7Z3NJUQMNOGPTIHQNJXSHSWVAMXAIBHK2A7KBU======'

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
    file_path = "C:/prtg/output.xml"
    if isinstance(response, str):
        with open(file_path, "w") as file:
            file.write(response)
        print(f"XML data saved to {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")



