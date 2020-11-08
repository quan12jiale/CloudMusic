import re
import json
import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    #'Accept-Encoding': 'gzip,deflate,sdch', # 这行的header在qt上使用返回的数据会出错
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

ids = 108795 #歌曲林俊杰的《曹操》的id
url = 'http://music.163.com/api/song/lyric?os=osx&id={0}&lv=-1&kv=-1&tv=-1'.format(
            ids)
sessions = requests.session()
rawHtml = sessions.get(url, headers=headers) #需要有headers,不然KeyError: 'lrc'
html = json.loads(rawHtml.text)
x = html['lrc']
lyric = html['lrc']['lyric']

def getLyric(rawLyric):
    # copu from https://github.com/wn0112/PPlayer
    lrc = rawLyric

    r1 = re.compile("\[(\d{2}:\d{2}(.\d+)?)\]")
    r2 = re.compile("\[\d+:+.+\](.*)")
    r3 = re.compile("\[offset:(-?\d+)\]")
    item = []
    lrc_lst = []
    offset = 0
    for line in lrc:
        times = r1.findall(line)
        lrc_words = r2.findall(line)
        if lrc_words:
            lrc_words = lrc_words[0]
        else:
            lrc_words = []

        if len(lrc_words) and lrc_words[0].rstrip():
            for i in times:
                item.append(i[0])
                item.append(lrc_words)
                lrc_lst.append(item)
                item = []
    lrc_lst.sort()

    return lrc_lst
result = lyric.split('\n')

lrc_lst = getLyric(result)
