import requests

auth_url ='https://dummyjson.com/auth/login';
auth_payload = {
    "username":"emilys",
    "password":"emilyspass"
}
headers= { 'Content-Type': 'application/json' }
auth_reesposne = requests.post(
    auth_url,
    json=auth_payload,
    headers=headers)

if auth_reesposne.status_code == 200:
    token = auth_reesposne.json();
    print(token['accessToken'])
    if not token:
        raise ValueError('Authentication Successful but not get teh token')
else:
    raise Exception("Auth failed",auth_reesposne.text)

user_url = 'https://dummyjson.com/auth/me'

headers = {
    'Authorization': f'Bearer {token}'
}

user_response = requests.get(user_url, headers=headers)

if user_response.status_code == 200:
    print(user_response.json())
else:
    raise Exception("Error",user_response.text)