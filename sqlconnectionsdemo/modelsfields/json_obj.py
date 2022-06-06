import requests
import json

URL = "http://127.0.0.1:8000/model/dataCreate/"

data = {
    'first_name':'Rohit',
    'last_name':'GHUle'
}

json_data = json.dumps(data)

post_request = requests.post(url=URL,data=data)

print(post_request)