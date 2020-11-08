import json
import requests

cookies = {
    #'appver': '2.1.2.184499',
    'os': 'pc',
    #'channel': 'netease',
}

year=2015
month=4
area='ALL'
url = 'http://music.163.com/api/discovery/new/albums/area?year=%d&month=%d&area=%s&type=hot&offset=0&total=true&limit=20&rcmd=true' \
    % (year, month, area)
    
sessions = requests.session()
rawHtml = sessions.get(url, cookies=cookies) #需要有cookies,不然返回码为403
html = json.loads(rawHtml.text)
res = html['monthData']
