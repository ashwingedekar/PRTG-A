import requests
import pandas as pd
from io import StringIO
import os

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id=10108&avg=0&sdate=2024-01-19-15-30-00&edate=2024-01-19-15-54-00&username=Ashwin.Gedekar&passhash=3422185132'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")

else:
    print(f"Error: {response.status_code} - {response.text}")
