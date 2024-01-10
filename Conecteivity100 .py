import requests
response = requests.get("https://192.168.99.100:10443/api/table.xml?content=sensors&columns=sensor&apitoken=YQMBHWIMJ443LJHCEYCPDT6344SCS4G2XUQEYDFQTU======")
print(response)


