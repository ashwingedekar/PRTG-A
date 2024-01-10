import requests

url = 'https://jp-vivekp-40-58.comtelindia.com/api/table.json?content=sensors&columns=sensor'
sensor_id = '1003'

params = {
    'id': sensor_id,
    'count': 1000,
    'columns': 'datetime,value_',
}

# Replace 'prtgadmin' and 'prtgadmin' with your PRTG username and password
username = 'prtgadmin'
password = 'prtgadmin'

response = requests.get(url, params=params, auth=(username, password))

if response.status_code == 200:
    data = response.json()
    # Process data as needed
else:
    print(f'Error: {response.status_code}')
    print(response.text)  # Print the response content for more details
