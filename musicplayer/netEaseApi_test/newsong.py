import json
import requests

cookies = {
    #'appver': '2.1.2.184499',
    'os': 'pc',
    #'channel': 'netease',
}

areaID=0
offset=0
total='true'
limit=100
url = 'http://music.163.com/api/discovery/new/songs?areaId=%d&offset=%d&total=%s&limit=%d' %\
    (areaID, offset, total, limit)

sessions = requests.session()
rawHtml = sessions.get(url, cookies=cookies) #需要有cookies,不然返回码为403
html = json.loads(rawHtml.text)
res = html['data']
