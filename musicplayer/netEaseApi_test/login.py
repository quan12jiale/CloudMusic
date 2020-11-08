# -*- coding: utf-8 -*-
from encode import encrypted_request
import json
import hashlib
import requests

#%%
username = '15733229885'
password = '2b137945'
password = password.encode()
md5 = hashlib.md5()
md5.update(password)
password = md5.hexdigest()

#%%
data = {'rememberLogin': 'true', 'password': password}
data['phone'] = username
data = encrypted_request(data)

#%%
    
sessions = requests.session()
url = 'http://music.163.com/weapi/login/cellphone?csrf_token='
rawHtml = sessions.post(url, data=data)
html = json.loads(rawHtml.text)
