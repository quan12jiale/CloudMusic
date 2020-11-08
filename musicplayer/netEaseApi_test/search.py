from encode import encrypted_request
import json
import requests

#%%
s = '清明雨上'
offset=0
limit=100
stype=1
data = {
    's': s,
    'offset': str(offset),
    'limit': str(limit),
    'type': str(stype)
}
text = json.dumps(data)
data = encrypted_request(data)

#%%
 
sessions = requests.session()
url = 'http://music.163.com/weapi/cloudsearch/get/web'
rawHtml = sessions.post(url, data=data)
html = json.loads(rawHtml.text)
result = html['result']
