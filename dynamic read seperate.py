import requests
import pandas as pd
from io import StringIO

# Read server, username, and passhash from the first file
with open("server_parameters.txt", "r") as file:
    server_parameters = dict(line.strip().split("=") for line in file)

# Read sdate and edate from the second file
with open("date_parameters.txt", "r") as file:
    date_parameters = dict(line.strip().split("=") for line in file)

# Read sensorid from the third file
with open("sensorid.txt", "r") as file:
    sensor_id = file.read().strip()

# Read max and min flags from the fourth file
#with open("max_min_flags.txt", "r") as file:
 #   max_flag, min_flag = map(int, file.read().strip().split(","))

# Read max and min flags from the fourth file
with open("max_min_flags.txt", "r") as file:
    flags = dict(line.strip().split("=") for line in file)
# Extract max and min flags
max_flag = int(flags.get("max", 0))  # Get value for 'max', default to 0 if not found
min_flag = int(flags.get("min", 0))  # Get value for 'min', default to 0 if not found
# Build API endpoint
api_endpoint = f'https://{server_parameters["server"]}/api/historicdata.csv?id={sensor_id}&avg={server_parameters["avg"]}&sdate={date_parameters["sdate"]}&edate={date_parameters["edate"]}&username={server_parameters["username"]}&passhash={server_parameters["passhash"]}'

# Make API request
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
            if max_flag == 1 and min_flag == 0:
                max_raw_speed_row = selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmax()]
                print(f"Maximum Traffic Total (Speed)(RAW):")
                print(f"id={sensor_id}")
                print(max_raw_speed_row)
            elif max_flag == 0 and min_flag == 1:
                min_raw_speed_row = selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmin()]
                print(f"Minimum Traffic Total (Speed)(RAW):")
                print(f"id={sensor_id}")
                print(min_raw_speed_row)
            elif max_flag == 1 and min_flag == 1:
                print(f"Both Maximum and Minimum Traffic Total (Speed)(RAW):")
                print(f"id={sensor_id}")
                print(selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmax()])
                print(selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmin()])
            else:
                print("Invalid combination of max and min flags.")
        else:
            print("No non-NaN values found in 'Traffic Total (Speed)(RAW)'.")
    
    except Exception as e:
        print(f"Error processing CSV data: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
