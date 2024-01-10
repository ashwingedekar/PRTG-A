import requests
import xml.etree.ElementTree as ET

def check_connection(url, params, headers):
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Request Error: {err}"

base_url = 'https://jp-vivekp-40-58.comtelindia.com/api/getobjectstatus.htm?id=2466&name=message'

api_token = '4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======'

# Define parameters for the API call
params = {
    'content': 'sensortree',
}

# Add API token to headers
headers = {
    'Authorization': f'Bearer {api_token}',
}

url = f"{base_url}"

result = check_connection(url, params, headers)

if result:
    print("Connected successfully!")
    # Rest of your code...
else:
    print("Error during connection.")
