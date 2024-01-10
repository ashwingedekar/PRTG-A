import requests

def check_connection(url, params):
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return None

base_url = 'https://jp-vivekp-40-58.comtelindia.com/api/getobjectstatus.htm?id=2466&name=message'

api_token = '4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======'

# Define parameters for the API call
params = {
    'content': 'sensortree',
    'username': 'prtgadmin',  # Replace with your PRTG username
    'password': 'prtgadmin',  # Replace with your PRTG password
}

# Add API token to params if it's not provided in the headers
if 'token' not in params:
    params['token'] = api_token

url = f"{base_url}"

result = check_connection(url, params)

if result:
    print("Connected successfully!")
    print("Response:")
    print(result)
else:
    print("Error during connection.")
