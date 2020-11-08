import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}

def get( url, **kwargs):
    if not kwargs.get('headers'):
        kwargs['headers'] = headers
    return requests.get(url, **kwargs) # 

url = 'http://p2.music.126.net/aNF-E4PeUu1lQUoIMDFj3g==/18689498650903813.jpg'

rawHtml =get(url).content
print(len(rawHtml))
