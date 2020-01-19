import jieba
import time
print(time.asctime(time.localtime(time.time())))
txt = open("danmus.txt", encoding="utf-8").readlines()
aim = {}
for cell in txt:
    content, date = cell.split('\t')
    temp = aim.get(date[:-3], [])
    temp.append(content)
    aim[date[:-3]] = temp
stopwords = [line.strip() for line in open("stop_words.txt", encoding="utf-8").readlines()]
jieba.load_userdict('ck.txt')
jieba.load_userdict('acg0.txt')
jieba.load_userdict('acg1.txt')
jieba.load_userdict('acg2.txt')
jieba.load_userdict('acg3.txt')
jieba.load_userdict('acg4.txt')
jieba.load_userdict('acg5.txt')
jieba.load_userdict('acg6.txt')

with open('danmu_an.csv', 'a+', encoding='utf-8') as f:
    f.write("name,value,date\n")
for txt_date in aim:
    words = jieba.lcut(" ".join(aim[txt_date]))
    counts = {}
    for word in words:
        word = word.upper()
        if word not in stopwords:
            if word == '\n' or word == '　' or word == ' ' or (len(word) <= 1 and (word != '草' and word != '艹')):
                if word == '坐':
                    pass
                else:
                    continue
            if word == '哈哈哈哈':
                word = '哈哈哈'
            if word == '哔哩哔哩':
                word = '哔哩哔哩(゜-゜)つロ干杯~'
            if word == '干杯':
                word = '哔哩哔哩(゜-゜)つロ干杯~'
            if word == '66':
                word = '666'
            if word == '999':
                word = '99'
            if word == 'POWER':
                word = 'POWER UP'
            if word == 'CCC':
                word = 'CC'
            if word == 'CCCC':
                word = 'CC'
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in items:
        word, count = i
        if word == '' or count <= 1:
            continue
        word.replace('，', ',')
        with open('danmu_an.csv', 'a+', encoding='utf-8') as f:
            f.write(word + "," + str(count) + "," + txt_date +'0分\n')
print(time.asctime(time.localtime(time.time())))