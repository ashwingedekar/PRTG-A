import requests

api_endpoint = 'https://tp-prtg-101-100.comtelindia.com:10443//api/table.xml?content=sensors&columns=objid,group,device,sensor,status,message,lastvalue,priority,favorite&username=Ashwin.Gedekar&passhash=1815236212'

# Make the API request
response = requests.get(api_endpoint)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    lines = response.text.split('\n')
    for line in lines:
        parts = line.split(',')
        # Skip the RAW values and print only every other value
        print(','.join(parts[::2]))
    
    file_path = "C:/prtg/output001.xml"
    if isinstance(response.text, str):
        with open(file_path, "w") as file:
            file.write(response.text)
        print(f"XML data saved to {file_path}")
else:
    print(f"Error: {response.status_code} - {response.text}")
