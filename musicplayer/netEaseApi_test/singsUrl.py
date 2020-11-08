from encode import encrypted_request
import json
import requests

ids = [108795, 108796]
data = {'csrf_token': '', 'ids': ids, 'br': 999000}
data = encrypted_request(data)

sessions = requests.session()
url = "http://music.163.com/weapi/song/enhance/player/url"
rawHtml = sessions.post(url, data=data)
html = json.loads(rawHtml.text)['data']
