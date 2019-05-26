import requests
import json

url = 'https://〇〇◯.appspot.com/'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(r.text)