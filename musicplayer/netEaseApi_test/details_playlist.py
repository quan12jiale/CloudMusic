import json
import requests

ids = 3081025492
url = 'http://music.163.com/api/playlist/detail?id={0}' .format(ids)

sessions = requests.session()
rawHtml = sessions.get(url)
html = json.loads(rawHtml.text)
res = html['result']
