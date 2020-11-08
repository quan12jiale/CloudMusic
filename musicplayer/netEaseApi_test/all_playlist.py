# -*- coding: utf-8 -*-
import json
import requests
import urllib.parse

cat='全部歌单'
types='all'
offset=0
index=1
url = 'http://music.163.com/api/playlist/list?cat=%s&type=%s&order=%s&offset=%d&total=true&limit=30&index=%d'\
    % (urllib.parse.quote(cat), types, types, offset, index)
            
sessions = requests.session()
rawHtml = sessions.get(url)
html = json.loads(rawHtml.text)
res = html['playlists']
