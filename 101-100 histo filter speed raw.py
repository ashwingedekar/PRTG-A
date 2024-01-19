import requests
import pandas as pd
from io import StringIO

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id=10108&avg=0&sdate=2024-01-19-11-30-00&edate=2024-01-19-12-00-00&username=Ashwin.Gedekar&passhash=3422185132'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")

    file_path = "C:/prtg/output.csv"
    
    try:
        # Use pandas to read the CSV data
        df = pd.read_csv(StringIO(response.text))

        # Clean up the column names (remove leading and trailing spaces)
        df.columns = df.columns.str.strip()

        # Extract only the specified columns
        selected_columns = ["Traffic Total (Speed)", "Traffic Total (Speed)(RAW)"]
        selected_data = df[selected_columns]

        # Save the extracted columns to a new CSV file
        extracted_file_path = "C:/prtg/extracted_traffic_data.csv"
        selected_data.to_csv(extracted_file_path, index=False)
        
        print(f"Extracted specified columns saved to {extracted_file_path}")
    
    except Exception as e:
        print(f"Error processing CSV data: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
