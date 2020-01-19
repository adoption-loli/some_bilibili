import requests
import json
import time

url = "https://api.bilibili.com/x/activity/bnj2020/main"

headers = {
    'Accept': "*/*",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Connection': "keep-alive",
    'Cookie': "buvid3=0E9ABA3E-A3AC-4DA0-B9B1-3CE5A32E14B984617infoc; LIVE_BUVID=AUTO3715504587901812; sid=ifbtlz7e; CURRENT_FNVAL=16; fts=1550537477; im_notify_type_12153382=0; stardustpgcv=0606; rpdid=|(JYYkR|uJu|0J'ull~|llRY|; innermark=1; arrange=matrix; deviceFingerprint=17e0e9e3919a0800acc26deb85ca6aa2; _uuid=AEE9D86B-A40D-88D1-189E-B2FA184BFF0C67541infoc; canvasFp=a5c463056dcbbf3b31b0a6eb7380521f; webglFp=7b8e15bd6c9ca5d1bd66ab0526f9301f; screenInfo=1920*1080*24; feSign=17e0e9e3919ad800acc26deb85ca6aa2; payParams=%7B%22createIp%22%3A%22223.152.39.234%22%2C%22customerId%22%3A10007%2C%22deviceType%22%3A1%2C%22feeType%22%3A%22CNY%22%2C%22notifyUrl%22%3A%22http%3A//api.bilibili.co/pgc/internal/pay/sponsor/order/notify/1%22%2C%22orderCreateTime%22%3A1564750729000%2C%22orderExpire%22%3A3600%2C%22orderId%22%3A%2220190802205839822%22%2C%22originalAmount%22%3A500%2C%22payAmount%22%3A500%2C%22productId%22%3A%2265%22%2C%22returnUrl%22%3A%22https%3A//www.bilibili.com/bangumi/play/ep199942%22%2C%22serviceType%22%3A0%2C%22showTitle%22%3A%22%u627F%u5305-%u300AComic%20Girls%u300B%22%2C%22sign%22%3A%223a9919aacc0344aecbb6f55a6ea5b330%22%2C%22signType%22%3A%22MD5%22%2C%22timestamp%22%3A1564750729000%2C%22traceId%22%3A%221da0a9a6-bded-46ed-b039-fd4a9673a4fa%22%2C%22uid%22%3A12153382%2C%22version%22%3A%221.0%22%7D; UM_distinctid=16cb4347541130-09e07ce7f27324-7373e61-1fa400-16cb434754245d; im_seqno_12153382=91145; im_local_unread_12153382=0; stardustvideo=1; laboratory=1-1; _ga=GA1.2.100957876.1569680124; kfcFrom=message; from=ticket_home; balh_season_ss28686=1; balh_season_ep285211=1; dy_spec_agreed=1; balh_season_ss28019=1; route=; DedeUserID=12153382; DedeUserID__ckMd5=c82e9372437992e2; msource=pc_web; SESSDATA=f8d97166%2C1579446769%2C2eecb3c1; bili_jct=fafe202a594c34b3efa0abee15a9f049; INTVER=1; CURRENT_QUALITY=112; bp_t_offset_12153382=346072165315282918; bsource=2020bnjbt, buvid3=0E9ABA3E-A3AC-4DA0-B9B1-3CE5A32E14B984617infoc; LIVE_BUVID=AUTO3715504587901812; sid=ifbtlz7e; CURRENT_FNVAL=16; fts=1550537477; im_notify_type_12153382=0; stardustpgcv=0606; rpdid=|(JYYkR|uJu|0J'ull~|llRY|; innermark=1; arrange=matrix; deviceFingerprint=17e0e9e3919a0800acc26deb85ca6aa2; _uuid=AEE9D86B-A40D-88D1-189E-B2FA184BFF0C67541infoc; canvasFp=a5c463056dcbbf3b31b0a6eb7380521f; webglFp=7b8e15bd6c9ca5d1bd66ab0526f9301f; screenInfo=1920*1080*24; feSign=17e0e9e3919ad800acc26deb85ca6aa2; payParams=%7B%22createIp%22%3A%22223.152.39.234%22%2C%22customerId%22%3A10007%2C%22deviceType%22%3A1%2C%22feeType%22%3A%22CNY%22%2C%22notifyUrl%22%3A%22http%3A//api.bilibili.co/pgc/internal/pay/sponsor/order/notify/1%22%2C%22orderCreateTime%22%3A1564750729000%2C%22orderExpire%22%3A3600%2C%22orderId%22%3A%2220190802205839822%22%2C%22originalAmount%22%3A500%2C%22payAmount%22%3A500%2C%22productId%22%3A%2265%22%2C%22returnUrl%22%3A%22https%3A//www.bilibili.com/bangumi/play/ep199942%22%2C%22serviceType%22%3A0%2C%22showTitle%22%3A%22%u627F%u5305-%u300AComic%20Girls%u300B%22%2C%22sign%22%3A%223a9919aacc0344aecbb6f55a6ea5b330%22%2C%22signType%22%3A%22MD5%22%2C%22timestamp%22%3A1564750729000%2C%22traceId%22%3A%221da0a9a6-bded-46ed-b039-fd4a9673a4fa%22%2C%22uid%22%3A12153382%2C%22version%22%3A%221.0%22%7D; UM_distinctid=16cb4347541130-09e07ce7f27324-7373e61-1fa400-16cb434754245d; im_seqno_12153382=91145; im_local_unread_12153382=0; stardustvideo=1; laboratory=1-1; _ga=GA1.2.100957876.1569680124; kfcFrom=message; from=ticket_home; balh_season_ss28686=1; balh_season_ep285211=1; dy_spec_agreed=1; balh_season_ss28019=1; route=; DedeUserID=12153382; DedeUserID__ckMd5=c82e9372437992e2; msource=pc_web; SESSDATA=f8d97166%2C1579446769%2C2eecb3c1; bili_jct=fafe202a594c34b3efa0abee15a9f049; INTVER=1; CURRENT_QUALITY=112; bp_t_offset_12153382=346072165315282918; bsource=2020bnjbt; LIVE_BUVID=AUTO3215792377908209",
    'DNT': "1",
    'Host': "api.bilibili.com",
    'Origin': "https://www.bilibili.com",
    'Referer': "https://www.bilibili.com/blackboard/xianxing2020bnj.html?bsource=2020bnjbt&spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.38&anchor=game",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Site': "same-site",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",
    'Cache-Control': "no-cache",
    'Postman-Token': "dfd26c8d-9cfa-4749-8429-ffeaaf05daae,4ada4f92-0043-431d-9612-9d88f39c8b22",
    'cache-control': "no-cache"
    }
while True:
    try:
        response = requests.request("GET", url, headers=headers)
        info = json.loads(response.text)
        value = info['data']['value']
        print(value)
        with open('huoguo.txt', 'a+', encoding='utf-8') as f:
            f.write(str(value) + ',' + time.strftime("%d{d}%H{h}%M{m}", time.localtime()).format(d='日', h='时', m='分')+'\n')
        time.sleep(60)
    except:
        print('遇到了一次错误')