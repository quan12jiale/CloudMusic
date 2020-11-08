import re
import requests

headers = {
    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
   # 'Connection': 'keep-alive',
   # 'Pragma': 'no-cache',
   # 'Cache-Control': 'no-cache',
    #'Accept-Encoding': 'gzip,deflate,sdch', # 这行的header在qt上使用返回的数据会出错
  #  'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

songId = 29953681 #歌曲林俊杰的《曹操》的id 108795
url = 'http://music.163.com/song?id={}'.format(songId)

sessions = requests.session()
rawHtml = sessions.get(url, headers=headers) #需要有headers
html = rawHtml.text
print(len(html))
#%% 
containedUl = re.findall(
    r'<ul class="m-rctlist f-cb">[.\s\S]+?</ul>', rawHtml.text)
if not containedUl:
    containedUl = ''
else:
    containedUl = containedUl[0]
playlists = set(re.findall(r'data-res-id="(.+)"', containedUl))

# 字符串索引13081：keep 跑步歌单『前方高能』
# 字符串索引13835：说不出名字的那些经典英文歌
# 字符串索引14619：78529193 健身力量增肌有氧减脂必备 | 持续更新
