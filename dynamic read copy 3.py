import requests
import pandas as pd
from io import StringIO

with open("parameters.txt", "r") as file:
    parameters = dict(line.strip().split("=") for line in file)

api_endpoint = f'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id={parameters.get("id")}&avg={parameters.get("avg")}&sdate={parameters.get("sdate")}&edate={parameters.get("edate")}&username={parameters.get("username")}&passhash={parameters.get("passhash")}'

response = requests.get(api_endpoint)

if response.status_code == 200:
    print("Request successful!")

    try:
        df = pd.read_csv(StringIO(response.text))

        df.columns = df.columns.str.strip()

        selected_columns = ["Date Time", "Traffic Total (Speed)", "Traffic Total (Speed)(RAW)"]
        selected_data = df[selected_columns]

        selected_data["Traffic Total (Speed)(RAW)"] = pd.to_numeric(selected_data["Traffic Total (Speed)(RAW)"], errors='coerce')

        selected_data = selected_data.dropna(subset=["Traffic Total (Speed)(RAW)"])

        if not selected_data.empty:
            max_raw_speed_row = selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmax()]

          
            min_raw_speed_row = selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmin()]

       
            print(f"Maximum Traffic Total (Speed)(RAW):")
            print(f"id={parameters.get('id')}")
            print(max_raw_speed_row)

            print(f"Minimum Traffic Total (Speed)(RAW):")
            print(f"id={parameters.get('id')}")
            print(min_raw_speed_row)

        else:
            print("No non-NaN values found in 'Traffic Total (Speed)(RAW)'.")
    
    except Exception as e:
        print(f"Error processing CSV data: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
