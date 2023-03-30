import os

import pytest, requests, json
import yaml

from common.yaml_util import YamlUtil


class TestQuest:
    def get_pass(self):
        url = "http://192.168.66.189:5700/open/auth/token"
        data = {
            "client_id": "_tOi5uqRN1S4",
            "client_secret": "rTl1_ypWCeUDA5bhj8C3H9ez"
        }
        res = requests.get(url, params=data)
        # 将token存入到文件中去
        YamlUtil().write_yaml({"token": res.json()["data"]["token"]})

    """
    获取token
    """

    def ge_token(self):
        url = "http://192.168.66.189:5700/api/user/login"
        data = {
            "username": "root",
            "password": "774522"
        }
        r = requests.post(url, data=data)
        # 将token存入到文件中去
        YamlUtil().write_yaml({"token": r.json()["data"]["token"]})

    # 获取所有环境变量账号密码token
    def ge_eves(self):
        url = "http://192.168.66.189:5700/api/envs"
        data = {
            "Authorization": "Bearer " + YamlUtil().read_yaml("token")
        }
        res = requests.get(url, headers=data)
        try:
            with open("E:\\python\\接口自动化学习\\1-100\\青龙面板测试\\所有的环境变量.txt", "w", encoding="utf-8") as f:
                eves = {res.json()["data"][0]["name"]: res.json()["data"][0]["value"]}
                yaml.dump(data=eves, stream=f)
        except (FileNotFoundError, OSError):
            print("没有这个文件夹")

        # 获取所有环境变量应用token

    def get_eves(self):
        url = "http://192.168.66.189:5700/open/envs"
        data = {
            "Authorization": "Bearer " + YamlUtil().read_yaml("token")
        }
        res = requests.get(url, headers=data)
        try:
            with open("E:\\python\\接口自动化学习\\1-100\\青龙面板测试\\所有的环境变量.txt", "w", encoding="utf-8") as f:
                eves = {res.json()["data"][0]["name"]: res.json()["data"][0]["value"]}
                yaml.dump(data=eves, stream=f)
        except (FileNotFoundError, OSError):
            print("没有这个文件夹")
