import json
import requests

URL = "http://127.0.0.1:8000/apicreate/"

data = {
    'first_name':'sonam',
    'last_name':'gupta',
    'desc':'Sonam gupta bewafa nhi hai'
}
data_json_dumps = json.dumps(data)
r = requests.post(url=URL,data=data_json_dumps)

data_request = r.json()
print(data_request)