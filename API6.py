import requests
import xml.etree.ElementTree as ET

def check_connection(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params)
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

url = 'https://jp-vivekp-40-58.comtelindia.com/api/table.xml'
api_token = '4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======'

params = {
    'content': 'sensors',
    'columns': 'sensor',
    'apitoken': api_token,
}

headers = {
    'Content-Type': 'application/json',
}

result = check_connection(url, headers, params)

if result:
    print("Connected successfully!")

    # Parse XML response
    root = ET.fromstring(result)
    
    # Find the sensor with ID 1004
    target_sensor_id = '1004'
    target_sensor = root.find(f'.//sensor[@id="{target_sensor_id}"]')

    if target_sensor is not None:
        # Process data for the specific sensor
        print(f"Data for Sensor ID {target_sensor_id}:")
        print(ET.tostring(target_sensor).decode())
    else:
        print(f"Sensor with ID {target_sensor_id} not found.")
else:
    print("Error during connection.")
