import pytest
import requests
import json


# 发送get请求
# def get(url, params=None, **kwargs):
def close_databases():
    print("关闭数据库")


class TestQuest:
    access_token = ""

    def test_get_token(self):
        url = "https://oauth.cnblogs.com/connect/token"
        data = {
            "client_id": "210d0d6e-e5cb-48bf-a5dd-f42c08e91cea",
            "client_secret": "lsf2Ovxl0cIxC75qsXhk-eUaPBN6VTBAKayEMvbY0Ajku8e2G6fBlcugnozXnI_JF4160o7XvViwywOC",
            "grant_type": "client_credentials",
        }
        rep = requests.post(url, data=data)
        print(rep.json())
        access_token = rep.json()["access_token"]
        return access_token

    # def test_use_token(self):
    #     self.test_get_token(self)
    def q_qq(self, conn_database):
        print("qqq" + TestQuest.access_token)

    def q_a(self, conn_database):
        print("qqq")



