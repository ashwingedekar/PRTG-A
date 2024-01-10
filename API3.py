import requests

def check_connection(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return None

url = 'url = https://jp-vivekp-40-58.comtelindia.com/api/table.json?content=sensors&columns=sensor'
sensor_id = '1003'
api_key = '4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======'

params = {
    'id': sensor_id,
    'count': 1000,
    'columns': 'datetime,value_',
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

result = check_connection(url, headers, params)

if result:
    print("Connected successfully!")
    # Process data as needed
    print(result)
else:
    print("Error during connection.")
