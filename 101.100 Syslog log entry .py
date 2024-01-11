import pandas as pd
import json
import requests

# API endpoint
api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=messages&id=3022&start=0&filter_drel=7days&columns=objid,datetime,type,name,status,messageid=3022&username=Ashwin.Gedekar&passhash=3422185132'
#/api/table.xml?content=messages&id=3022&start=0&filter_drel=7days&columns=objid,datetime,type,name,status,message
# Make the API request
response = requests.get(api_endpoint)
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    print(response.text)
else:
    print(f"Error: {response.status_code} - {response.text}")
