import requests
import pandas as pd
from io import StringIO

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id=10017&avg=5&sdate=2024-02-09-13-40-00&edate=2024-02-09-13-45-00&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")

    try:
        # Use pandas to read the CSV data
        df = pd.read_csv(StringIO(response.text))

        # Clean up the column names (remove leading and trailing spaces)
        df.columns = df.columns.str.strip()

        # Extract specified columns along with "Date Time"
        selected_columns = ["Date Time", "Traffic Total (Speed)", "Traffic Total (Speed)(RAW)"]
        selected_data = df[selected_columns]

        # Convert "Traffic Total (Speed)(RAW)" to numeric type
        selected_data["Traffic Total (Speed)(RAW)"] = pd.to_numeric(selected_data["Traffic Total (Speed)(RAW)"], errors='coerce')

        # Drop rows with NaN values in "Traffic Total (Speed)(RAW)"
        selected_data = selected_data.dropna(subset=["Traffic Total (Speed)(RAW)"])

        # Check if the DataFrame is not empty
        if not selected_data.empty:
            # Save the selected data to a CSV file
            output_csv_file = "selected_data.csv"
            selected_data.to_csv(output_csv_file, index=False)
            print(f"Selected data has been saved to {output_csv_file}")
        else:
            print("No non-NaN values found in 'Traffic Total (Speed)(RAW)'.")

    except Exception as e:
        print(f"Error processing CSV data: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
