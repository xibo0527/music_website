import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
url = 'https://baike.baidu.com/item/CDN'

ret = requests.get(url,headers=headers).text
print(ret.encode('utf-8'))