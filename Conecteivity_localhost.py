import requests
response = requests.get("https://me-ncm-01.comtelindia.com:8061/api/json/v2/ncmdevice/listAllDevices?apiKey=004869eea1f43365a547efb9c410f75e")
#http://localhost:8060/api/json/v2/ncmdevice/listAllDevices?apiKey=004869eea1f43365a547efb9c410f75e
print(response)
