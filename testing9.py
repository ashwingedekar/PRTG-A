import requests
import pandas as pd
from io import StringIO

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&output=csvtable&columns=sensor,objid,parentid,device&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    
    # Convert CSV response to pandas DataFrame
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))

    # Extract the 'Parent ID' column
    parent_ids = df['Parent ID']

    # Specify the path for the Excel file
    excel_file_path = "C:/prtg/parent_ids.xlsx"

    # Save the parent IDs to Excel
    parent_ids.to_excel(excel_file_path, index=False)

    print(f"Parent IDs saved to {excel_file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")
