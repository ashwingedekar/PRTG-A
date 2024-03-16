import requests
import re

# Define the API endpoints
api_endpoint_warning = 'https://tp-prtg-101-100.comtelindia.com:10443/api/getobjectproperty.htm?id=9619&subtype=channel&subid=-1&name=limitmaxwarning&show=nohtmlencode&username=Ashwin.Gedekar&passhash=1815236212'
api_endpoint_error = 'https://tp-prtg-101-100.comtelindia.com:10443/api/getobjectproperty.htm?id=9619&subtype=channel&subid=-1&name=limitmaxerror&show=nohtmlencode&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request for Upper Warning Limit
response_warning = requests.get(api_endpoint_warning)

# Check if the request was successful (status code 200)
if response_warning.status_code == 200:
    # Extract the numeric value from the response text using regular expressions
    match_warning = re.search(r'<result>(\d+)</result>', response_warning.text)
    if match_warning:
        # Convert the value from bytes to megabits
        value_in_bytes_warning = int(match_warning.group(1))
        value_in_megabits_warning = value_in_bytes_warning * 8 / 1000000  # Convert bytes to megabits
        
        # Print the extracted value in megabits for Upper Warning Limit
        print(f"Upper Warning Limit: {value_in_megabits_warning:.2f} Mbps")
    else:
        print("No match found in the response text for Upper Warning Limit")
else:
    print(f"Error: {response_warning.status_code} - {response_warning.text}")

# Make the API request for Upper Error Limit
response_error = requests.get(api_endpoint_error)

# Check if the request was successful (status code 200)
if response_error.status_code == 200:
    # Extract the numeric value from the response text using regular expressions
    match_error = re.search(r'<result>(\d+)</result>', response_error.text)
    if match_error:
        # Convert the value from bytes to megabits
        value_in_bytes_error = int(match_error.group(1))
        value_in_megabits_error = value_in_bytes_error * 8 / 1000000  # Convert bytes to megabits
        
        # Print the extracted value in megabits for Upper Error Limit
        print(f"Upper Error Limit: {value_in_megabits_error:.2f} Mbps")
    else:
        print("No match found in the response text for Upper Error Limit")
else:
    print(f"Error: {response_error.status_code} - {response_error.text}")
