#import the modules
import requests
import json

url = 'http://gbmvsdrpn1/GBMDigital/api/Security/GetUserKey'
params = {"user": "roberto.cervantes@microsoft.com", "password": ".Gbm2014", "token": "", "hash": "", "deviceType": 1, "newPassword": "" }
headers = { "Content-Type": "Application/json", "X-Forwarded-For": "127.0.0.1", "GBMDigitalIdentityApp" : 1 }

def call(url, params, headers):
    print('calling: ' + url)
    try:    
        response = requests.post(url, data = json.dumps(params), headers=headers)
        print(response.json())
    except Exception as ex:
        print ('Unexpected error: ', ex)

call(url, params, headers)
