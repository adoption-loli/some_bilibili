import requests
import json
import time
from queue import Queue
import threading
from urllib.request import urlopen
from bs4 import BeautifulSoup


def find(i, q):
    url = "https://space.bilibili.com/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    try:
        session = requests.Session()
        aim_url = url+str(i)
        html = session.get(aim_url, headers=headers)
        bsObj = BeautifulSoup(html.text)
        name = bsObj.find("title").get_text()[:-35]
        if '御坂' in name:
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


def test(uid,q):
    try:
        if False:
            q.put(uid)
        else:
            q.put(None)
    except:
        pass


if __name__ == "__main__":
    q = Queue()
    uid = 1370000
    max_thread = 100
    print(time.asctime(time.localtime(time.time())))
    result = set()
    while uid < 1380000:
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