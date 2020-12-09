import requests
import json

data_json = json.dumps()

r = requests.post()
par = {"Keywords": "yoyoketang"}
r = requests.get("https://zzk.cnblogs.com/s/blogpost", params=par)

print(r.status_code)
# print(r.text)
# print(r.headers)
r.cookies
