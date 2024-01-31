import requests
import pandas as pd
from io import StringIO

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=devices&output=csvtable&columns=device,host,objid,parentid&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    print(response.text)
    
    # Parse the CSV-formatted data from the response
    csv_data = response.text.strip()

    # Convert CSV data to pandas DataFrame
    df = pd.read_csv(StringIO(csv_data))

    # Select only the required columns: Device, Host, ID
    selected_columns = ['Device', 'Host', 'ID']
    df_selected = df[selected_columns]

    # Specify the file path for the Excel file
    excel_file_path = "C:/prtg/devices_data.xlsx"

    # Save the selected data to Excel
    df_selected.to_excel(excel_file_path, index=False)

    print(f"Data saved to {excel_file_path}")
    
else:
    print(f"Error: {response.status_code} - {response.text}")
