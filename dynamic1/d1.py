import requests
import pandas as pd
from io import StringIO


# Read parameters from file
with open("server_address.txt", "r") as file:
    server_parameters = dict(line.strip().split("=") for line in file)



server_address = server_parameters.get("server", "")  # Get the value associated with the key "server"
print("Server address:", server_address)


with open("parameters.txt", "r") as file:
    parameters = dict(line.strip().split("=") for line in file)

with open("para.txt", "r") as file:
    para = dict(line.strip().split("=") for line in file)    



# Construct the API endpoint URL using the extracted dates
api_endpoint = f'https://{server_parameters.get("server")}/api/historicdata.csv?id={parameters.get("id")}&avg={parameters.get("avg")}&sdate={parameters.get("sdate")}&edate={parameters.get("edate")}&username={para.get("username")}&passhash={para.get("passhash")}'
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
            # Find the row with the maximum "Traffic Total (Speed)(RAW)"
            max_raw_speed_row = selected_data.loc[selected_data["Traffic Total (Speed)(RAW)"].idxmax()]

            # Print the result in the terminal
            print("Row with the maximum Traffic Total (Speed)(RAW):")
            print(max_raw_speed_row)
        else:
            print("No non-NaN values found in 'Traffic Total (Speed)(RAW)'.")
    
    except Exception as e:
        print(f"Error processing CSV data: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
    