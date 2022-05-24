import requests

url_string = "https://r016team04prod.computerlab.online"
response = requests.get(url_string, verify=False)

print(response.content)
