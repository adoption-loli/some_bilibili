import requests
import json
import time

url = "https://api.live.bilibili.com/xlive/web-room/v1/index/getInfoByRoom"

querystring = {"room_id": "544641"}

headers = {
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "81920df0-b165-41ce-8409-fedb6c9b8fb3,781deefc-ec83-4435-8d44-ddc7d98d45e1",
    'Host': "api.live.bilibili.com",
    'cookie': "LIVE_BUVID=AUTO3215792377908209",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
print('='*20)
print('开始待机...')
while True:
    try:
        if time.time() < 1579795200:
            time.sleep(60)
        else:
            print(time.asctime(time.localtime()), '开始采集')
            print('=' * 20)
            break
    except:
        print('等待时出错')

flag = 0
while True:
    try:
        flag += 1
        if flag % 60 == 0:
            print(time.strftime("%d{d}%H{h}%M{m}", time.localtime()).format(d='日', h='时', m='分'))
        response = requests.request("GET", url, headers=headers, params=querystring)
        info = json.loads(response.text)
        hot_point = info['data']['room_info']['online']
        with open('huoguo.txt', 'a+', encoding='utf-8') as f:
            f.write(str(hot_point) + ',' + time.strftime("%d{d}%H{h}%M{m}", time.localtime()).format(d='日', h='时', m='分') + '\n')
        time.sleep(1)
    except:
        print('出现一次错误')