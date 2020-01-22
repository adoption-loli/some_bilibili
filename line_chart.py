import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from matplotlib.pyplot import MultipleLocator

plt.rcParams['font.family']=['STFangsong']
x_major_locator=MultipleLocator(10)
with open('huoguo.txt', 'r', encoding='utf-8') as f:
    datas = f.readlines()
y = []
x = []
for cell in range(1, len(datas)):
    ty, tx = datas[cell].split(',')
    ty = int(ty) - int(datas[cell-1].split(',')[0])
    y.append(ty)
    x.append(tx[:-1])

plt.figure(figsize=(len(datas), 15))
plt.plot(x, y)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_ticks_position('right')
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.savefig('fix.jpg', dpi=300)
plt.show()



