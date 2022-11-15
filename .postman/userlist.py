#fetch userlist
import requests

URL = "https://github.com/newstudent632/demoapi"

print("search userlis")
user = input(">")
queryURL = URL + f"?username={user}"
responce = requests.get(queryURL)

print(responce.text)
