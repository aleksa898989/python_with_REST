import requests


response = requests.get("http://api.open-notify.org/astros.json")
if response.status_code == 200:
    json_response = response.json()
    json_file = open("file.json", "w")
    json_file.write(str(json_response))
    json_file.close()
    print("Success, data written to file!")
else:
    print("Error occurred! Status code: " + response.status_code)










