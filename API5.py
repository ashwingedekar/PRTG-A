import requests
import xml.etree.ElementTree as ET

def check_connection(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.text  # Return raw XML response
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    return None

# Updated PRTG URL and API token
url = 'https://jp-vivekp-40-58.comtelindia.com/api/table.xml'
api_token = '4NMXTANEV3HEFWYGISUQRIHS725KOOQWZ5EWWLCELE======'

params = {
    'content': 'sensors',
    'columns': 'sensor',
    'apitoken': api_token,
}

headers = {
    'Content-Type': 'application/xml',  # Adjusted to XML content
}

result = check_connection(url, headers, params)

if result:
    print("Connected successfully!")
    # Process data as needed
    root = ET.fromstring(result)
    # Now 'root' contains the root element of the XML response, and you can parse it accordingly
    # Example: print the tag of the root element
    print("Root Element Tag:", root.tag)
else:
    print("Error during connection.")
