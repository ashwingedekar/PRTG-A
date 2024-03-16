import requests


api_endpoint = 'https://prtg-99-102.comtelindia.com:10443/api/table.xml?content=sensortree&username=Ashwin.Gedekar&passhash=3639278600'


# Make the API request
response = requests.get(api_endpoint)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Request successful!")
    print("Response:")
    # Uncomment the line below to print the response text
    # print(response.text)
   
    
    # You can save the XML data to a file if needed
    # file_path = "C:/prtg/output55.xml"
    # if isinstance(response.text, str):
    #     with open(file_path, "w") as file:
    #         file.write(response.text)
    #     print(f"XML data saved to {file_path}") 
    
else:
    print(f"Error: {response.status_code} - {response.text}")
