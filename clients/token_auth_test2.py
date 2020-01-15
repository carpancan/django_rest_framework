import requests


def client():

    # credentials = {
    #     'username': 'resttest',
    #     'email': 'test@rest.com',
    #     'password1': 'changeme123456',
    #     'password2': 'changeme123456'
    # }
    #
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=credentials)

    token = 'Token 54dc48330274e494614951f35c38faa0d4f62569'
    headers = {
        'Authorization': token
    }
    response = requests.get('http://127.0.0.1:8000/api/profiles/', headers=headers)

    print('Status code: ', response.status_code)

    response_data = response.json()

    print(response_data)


if __name__ == '__main__':
    client()
