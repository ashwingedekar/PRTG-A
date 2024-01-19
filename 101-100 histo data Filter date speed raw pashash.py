import requests
import csv

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443/api/historicdata.csv?id=10108&avg=0&sdate=2024-01-19-11-30-00&edate=2024-01-19-12-00-00&username=Ashwin.Gedekar&passhash=3422185132'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")

    file_path = "C:/prtg/output.csv"
    
    try:
        # Assuming the response is a valid CSV, directly write it to a file
        with open(file_path, "w", newline='') as csv_file:
            csv_file.write(response.text)
        
        print(f"CSV data saved to {file_path}")
    
    except Exception as e:
        print(f"Error writing CSV data to file: {e}")

else:
    print(f"Error: {response.status_code} - {response.text}")
