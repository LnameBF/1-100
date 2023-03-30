import requests, json


class get_user:

    def get_pass(self):
        url = "http://192.168.66.189:5700/auth/token"
        data = {
            "client_id": "_tOi5uqRN1S4",
            "client_secret": "rTl1_ypWCeUDA5bhj8C3H9ez"
        }
        res = requests.get(url, params=data)
        print(res.text)

    def get_name(self):
        url = "http://192.168.66.189:5700/api/user/login"
        data = {
            "username": "root",
            "password": "774522"
        }
        r = requests.post(url, data=data)
        return r.json()["data"]["token"]

qinglong = get_user()
print("------------------")
s = qinglong.get_name()
print(s)