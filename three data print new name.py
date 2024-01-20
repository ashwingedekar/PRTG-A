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

    base_path = "C:/prtg/output.csv"
    
    try:
        # Use pandas to read the CSV data
        df = pd.read_csv(StringIO(response.text))

        # Clean up the column names (remove leading and trailing spaces)
        df.columns = df.columns.str.strip()

        # Extract specified columns along with "Date Time"
        selected_columns = ["Date Time", "Traffic Total (Speed)", "Traffic Total (Speed)(RAW)"]
        selected_data = df[selected_columns]

        # Check if the output file already exists
        counter = 1
        file_path = base_path
        while os.path.exists(file_path):
            file_path = f"C:/prtg/extracted_traffic_data_{counter}.csv"
            counter += 1

        # Save the extracted columns to the new CSV file
        selected_data.to_csv(file_path, index=False)
        
        print(f"Extracted specified columns saved to {file_path}")
    
    except Exception as e:
        print(f"Error processing CSV data: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
