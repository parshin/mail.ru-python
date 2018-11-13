import requests
import base64


def send_request():
    address = 'http://79.137.175.13/submissions/1/'
    user = 'alladin'
    password = 'opensesame'
    auth_str = '%s:%s' % (user, password)
    b64_auth = base64.b64encode(auth_str.encode()).decode("utf-8")
    headers = {'Authorization': 'Basic %s' % b64_auth}
    r = requests.post(address, headers=headers).json()
    print(r)


def send_secret_request():
    address = 'http://79.137.175.13/submissions/super/duper/secret/'
    user = 'galchonok'
    password = 'ktotama'
    auth_str = '%s:%s' % (user, password)
    b64_auth = base64.b64encode(auth_str.encode()).decode("utf-8")
    headers = {'Authorization': 'Basic %s' % b64_auth}
    r = requests.put(address, headers=headers).json()
    print(r)


if __name__ == '__main__':
    # send_request()
    send_secret_request()
