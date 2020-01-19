import time
import requests
import json


sleeptime = 0.5

def getdanmu(roomid, old_list):
    global sleeptime
    header = {
              'Referer': 'https://live.bilibili.com/284165?spm_id_from=333.334.b_62696c695f6c697665.13',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
              'cache-control': "no-cache",
              'Accept': "*/*",
              }
    headers = {
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "live.bilibili.com",
        'accept-encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache",
    }
    url = 'https://api.live.bilibili.com/ajax/msg'
    # session = requests.Session()
    data = {
        "roomid": roomid,
        "csrf_token": "",
        "csrf": "",
        "visit_id": "",
    }
    html = requests.post(url, headers=header, data=data)
    # html = session.get(url, headers=headers)
    # bsobj = bs4.BeautifulSoup(html.text)
    # pyperclip.copy(bsobj.find("span", {"class": "action-text v-middle live-skin-normal-text dp-i-block"}).get_text())
    # pyperclip.copy(html.text)
    result = json.loads(html.text)["data"]["room"]
    temp_list = []
    for cell in result:
        newdanmu_list = json.dumps({cell['text']: time.strftime("%d{d}%H{h}%M{m}", time.localtime(cell['check_info']['ts'])).format(d='日', h='时', m='分')})
        temp_list.append(newdanmu_list)
    if temp_list == old_list:
        pass
    else:
        for text_number in range(1, 11):
            # 创建for循环一次将1到10的数字赋给text_number
            if "".join(temp_list[:text_number]) in "".join(old_list):
                pass
            # 使用join方法以""为分割符提取temp_list切割后的列表的内容
            # 使用join方法以""为分割符提取old_list列表的内容
            # 比较内容是否相同，如果相同则跳过
            else:
                try:
                    old_list += temp_list[text_number - 1:]
                    now_temp = len(temp_list[text_number - 1:])
                    if now_temp == 10:
                        sleeptime *= 0.5
                    elif now_temp <= 2:
                        sleeptime *= 2
                    elif now_temp == 5:
                        sleeptime = 0.5
                    break
                except:
                    pass
    return old_list

def main():
    print('开始')
    global sleeptime
    while True:
        try:
            拜年祭 = "544641"
            roomid = "21302352"
            old_list = []
            max_danmu_temp = 100
            while True:
                if len(old_list) >= max_danmu_temp:
                    with open('danmus.txt', "a+", encoding='utf-8') as f:
                        for danmus in old_list[-int(max_danmu_temp/2):]:
                            danmus = json.loads(danmus)
                            f.write(list(danmus.keys())[0] + '\t' + list(danmus.values())[0] + '\n')
                    old_list = old_list[int(max_danmu_temp/2):max_danmu_temp]
                old_list = getdanmu(拜年祭, old_list)
                time.sleep(sleeptime)
        except:
            pass


if __name__ == "__main__":
    main()
