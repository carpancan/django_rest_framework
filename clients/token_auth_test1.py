import requests

def client():
    #credentials = {'username': 'admin', 'password': '123456'}

    #response = requests.post('http://127.0.0.1:8000/api/rest-auth/login/', data=credentials)

    #response_data = response.json()

    #print(response_data)

    headers = {"Authorization": "Token 5f632fa596b71d955948c2c7bb176404903b8379"}

    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('Status code: ', response.status_code)

    response_data = response.json()

    print(response_data)


if __name__ == '__main__':
    client()
