#import requests
#response = requests.get("https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&columns=sensor&apitoken=GJMJ23FVPUXRS4Q4PGZUR4EZXA4DUQDPJ5F3KDFEQY======")
#print(response)


#/api/getobjectproperty.htm?id=objectid&name=propertyname&show=nohtmlencode



#api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml'

#
import requests

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensortree&id=5584&username=Ashwin.Gedekar&passhash=440909494'

#3422185132  PRTG-99-102.comtelindia.com
#tp-prtg-101-100.comtelindia.com:10443
# Make the API request
response = requests.get(api_endpoint)


if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    print(response.text)
    
    file_path = "devices.xml"
    if isinstance(response.text, str):
        with open(file_path, "w") as file:
            file.write(response.text)
        print(f"XML data saved to {file_path}")
    
    
    
else:
    print(f"Error: {response.status_code} - {response.text}")



