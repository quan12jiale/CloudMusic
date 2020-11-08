from encode import encrypted_request
import json
import requests

uid = 536802748 # 536802748是我的网易云账号的实际id
offset = 0
limit = 1000
data = {'offset': offset, 'uid': uid, 'limit': limit, 'csrf_token': ''}
data = encrypted_request(data)

sessions = requests.session()
url = 'http://music.163.com/weapi/user/playlist'
rawHtml = sessions.post(url, data=data)
html = json.loads(rawHtml.text)['playlist']
print(len(rawHtml.text))