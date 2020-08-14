# -*- coding:utf-8 -*-
import requests
from random import randint

def get_token():
    headers = {"Content-Type": "application/json"}
    userinfo = {
        "PhoneNumber": "13338053699",
        "Password": "a123456"
    }
    url = "http://192.168.0.241:3005/api/Account/SignIn"
    response = requests.post(url, json=userinfo, headers=headers)
    response_json = response.json()
    token = "bearer "+response_json["result"]["token"]
    return token


def create_group():
    group_name = "分组" + str(randint(1000, 9999))
    print(group_name)pei
    return (group_name)

def add_group():
    headers = {"Content-Type": "application/json",
               "Authorization": get_token()}
    data = {
        "Type": 1,
        "GroupName": create_group()
    }
    url = "http://192.168.0.241:3005/api/QuickReplyGroup/Add"
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    print(response_json)

def get_group():
    headers = {"Content-Type": "application/json",
               "Authorization": get_token()}
    data = {
        "Type": 1
    }
    url = "http://192.168.0.241:3005/api/QuickReplyGroup/Get"
    response = requests.get(url, params=data, headers=headers)
    response_json = response.json()
    return response_json

def update_group():
    group_id = get_group()["result"][-1]["id"]
    group_name = get_group()["result"][-1]["groupName"]
    new_group_name = group_name+"修改"
    headers = {"Content-Type": "application/json",
               "Authorization": get_token()}
    data = {c
        "Id": group_id,
        "GroupName": new_group_name

    }
    url = "http://192.168.0.241:3005/api/QuickReplyGroup/Update"
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    print(response_json)

def delete_group():
    group_id = get_group()["result"][-1]["id"]
    print(group_id)
    headers = {"Content-Type": "application/json",
               "Authorization": get_token()}
    data = {"Id": group_id}
    url = "http://192.168.0.241:3005/api/QuickReplyGroup/Delete"
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    print(response_json)

if __name__ == '__main__':
      update_group()