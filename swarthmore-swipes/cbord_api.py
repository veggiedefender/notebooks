import requests

def authenticate(device_id, pin):
    auth_json = {
        "method": "authenticatePIN",
        "params": {
            "pin": pin,
            "deviceId": device_id,
            "systemCredentials":{
                "password": "NOTUSED",
                "userName": "get_mobile",
            }
        }
    }
    resp = requests.post('https://services.get.cbord.com/GETServices/services/json/authentication', json=auth_json)
    return resp.json()['response']

def get_transactions(session_id):
    transaction_json = {
        "method": "retrieveTransactionHistory",
        "params": {
            "queryCriteria": {
                "startingReturnRow": 0,
                "maxReturn": -1,
                "startDate": None,
                "endDate": None                
            },
            "paymentSystemType": 0,
            "sessionId": session_id
        }
    }
    resp = requests.post('https://services.get.cbord.com/GETServices/services/json/commerce', json=transaction_json)
    return resp.json()['response']['transactions']
