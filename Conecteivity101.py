import requests
response = requests.get("https://tp-prtg-101-100.comtelindia.com:10443/api/table.xml?content=sensors&columns=sensor&apitoken=3P2G7Z3NJUQMNOGPTIHQNJXSHSWVAMXAIBHK2A7KBU======")
print(response)
