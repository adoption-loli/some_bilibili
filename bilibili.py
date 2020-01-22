import requests
import json
import time
from queue import Queue
import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup


def find(i, q):
    url = "https://api.bilibili.com/x/space/acc/info"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    data = {
        'mid': str(i),
        'jsonp': 'jsonp',
    }
    try:
        html = requests.get(url,params=data)
        user_infomation = json.loads(html.text)['data']
        if '御坂' in user_infomation['name']:
            q.put(i)
        else:
            q.put(None)
    except:
        q.put(None)


def saveinfo(info):
    with open('userinfo.txt', 'a+') as f:
        for user in info:
            if user == None:
                continue
            info = user['mid'] + '\t' + user['name'] + '\t' + str(user['level_info']['current_level']) + '\t' + user[
                'face'] + '\n'
            f.write(info)


def main():
    q = Queue()
    uid = 1
    max_thread = 4
    print(time.asctime(time.localtime(time.time())))
    result = set()
    while uid < 10000:
        threads = []
        for i in range(max_thread):
            new_thread = threading.Thread(target=find, args=[uid+i, q])
            new_thread.start()
            threads.append(new_thread)
        for thread in threads:
            thread.join()
        for _ in range(max_thread):
            result.add(q.get())
        #saveinfo(result)
        uid += max_thread
    with open('userinfo.txt', 'a+') as f:
        f.write(json.dumps(list(result)))
    print(time.asctime(time.localtime(time.time())))


def demo(uid):
    url = "https://api.bilibili.com/x/space/acc/info"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    data = {
        'mid': str(uid),
        'jsonp': 'jsonp',
    }
    html = requests.get(url, params=data)
    print(html.text)
    print(type(html.text))

if __name__ == "__main__":
    main()