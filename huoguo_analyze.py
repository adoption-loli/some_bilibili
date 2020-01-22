import time

with open('huoguo.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

newdata = []

for cell in lines:
    value, date = cell.split(',')
    date = '2020-02-' + date[:2] + ' ' + date[3:5] + ':' + date[6:8] + ':00'
    date = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    date = int(time.mktime(date) * 1000)
    newdata.append(str(value) + ',' + str(date) + '\n')

with open('huoguo.txt', 'w', encoding='utf-8') as f:
    for cell in newdata:
        f.write(cell)