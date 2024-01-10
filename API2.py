import requests

# Full path to the certificate file
cert_path = 'C:\\Users\\ashwin.gedekar\\cert.pem'

url = 'https://192.168.40.58:443/api/table.json'
sensor_id = '1003'
api_key = 'L6K6SRND4B7T4OK6WTGPUGDC7IFNWRT7EPUSEQKQIM======'

params = {
    'id': sensor_id,
    'count': 1000,
    'columns': 'datetime,value_',
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}

# Make the request with SSL verification using the provided certificate
response = requests.get(url, headers=headers, params=params, verify=cert_path)

if response.status_code == 200:
    data = response.json()
    # Process data as needed
else:
    print(f'Error: {response.status_code}')
