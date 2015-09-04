#import the modules
import requests
import json

url = 'http://localhost/Get'
params = {"user": "roberto.cervantes@test.com", "password": ".sample", "token": "", "hash": "", "device": 1, "newPassword": "" }
headers = { "Content-Type": "Application/json", "X-Forwarded-For": "127.0.0.1", "App" : 1 }

def call(url, params, headers):
    print('calling: ' + url)
    try:    
        response = requests.post(url, data = json.dumps(params), headers=headers)
        print(response.json())
    except Exception as ex:
        print ('Unexpected error: ', ex)

call(url, params, headers)
