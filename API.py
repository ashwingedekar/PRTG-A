import requests

url = 'https://JP-VIVEKP-40-58.comtelindia.com/api/table.json'
sensor_id = '1003'
api_key = 'RKQULP4OJIU6RR4RANR4WVLQKAZOZRDRIFB3NJFPIA======'

params = {
    'id': sensor_id,
    'count': 1000,
    'columns': 'datetime,value_',
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}',
}



response = requests.get(url, headers=headers,params=params)



if response.status_code == 200:
    data = response.json()
    # Process data as needed
else:
    print(f'Error: {response.status_code}')
    
    
  #RKQULP4OJIU6RR4RANR4WVLQKAZOZRDRIFB3NJFPIA======