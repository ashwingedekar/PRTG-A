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

    # Print the columns to identify the correct column names
    print("Columns:", df.columns)

    # Adjust the column name accordingly
    # Replace 'objid' with the correct column name for sensor IDs
    # For example, if the correct column name is 'ID', use df['ID'] instead of df['objid']
    sensor_ids = df['ID']

    # Specify the path for the Excel file
    excel_file_path = "C:/prtg/sensor_ids.xlsx"

    # Save the sensor IDs to Excel
    sensor_ids.to_excel(excel_file_path, index=False)

    print(f"Sensor IDs saved to {excel_file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")
