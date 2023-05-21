import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

path = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\V2.0\opt_version2\\data.csv')
data = np.loadtxt(path, dtype=str, delimiter=',')
item, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12 = data[1:6,0],data[1:6,1],data[1:6,2],data[1:6,3],data[1:6,4],data[1:6,5],data[1:6,6],data[1:6,7],data[1:6,8],data[1:6,9],data[1:6,10],data[1:6,11],data[1:6,12]
m = data[0]

m1 = list(map(float, m1))
m2 = list(map(float, m2))
m3 = list(map(float, m3))
m4 = list(map(float, m4))
m5 = list(map(float, m5))
m6 = list(map(float, m6))
m7 = list(map(float, m7))
m8 = list(map(float, m8))
m9 = list(map(float, m9))
m10 = list(map(float, m10))
m11 = list(map(float, m11))
m12 = list(map(float, m12))
print(m, item, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12)

fig,ax = plt.subplots(figsize=(10, 8))
ax.grid(False)
ax.set_xlabel('Energy item/Hartree')
ax.set_ylabel('Energy value')

ax.plot(item, m1, marker = '.', color='r', alpha = 1, label='{}'.format(m[1]))
ax.plot(item, m2, marker = 'o', color='g', alpha = 1, label='{}'.format(m[2]))
ax.plot(item, m3, marker = 'v', color='b', alpha = 1, label='{}'.format(m[3]))
ax.plot(item, m4, marker = '^', color='black', alpha = 1, label='{}'.format(m[4]))
ax.plot(item, m5, marker = '<', color='orange', alpha = 1, label='{}'.format(m[5]))
ax.plot(item, m6, marker = '>', color='pink', alpha = 1, label='{}'.format(m[6]))
ax.plot(item, m7, marker = 's', color='gray', alpha = 1, label='{}'.format(m[7]))
ax.plot(item, m8, marker = 'p', color='lime', alpha = 1, label='{}'.format(m[8]))
ax.plot(item, m9, marker = '*', color='slateblue', alpha = 1, label='{}'.format(m[9]))
ax.plot(item, m10, marker = 'h', color='brown', alpha = 1, label='{}'.format(m[10]))
ax.plot(item, m11, marker = '+', color='deeppink', alpha = 1, label='{}'.format(m[11]))
ax.plot(item, m12, marker = 'x', color='cyan', alpha = 1, label='{}'.format(m[12]))

plt.rcParams.update({'font.size': 9}) 
fig.legend(loc = "upper right", bbox_to_anchor=(0.63,0.72))
plt.xticks(rotation=7)
plt.show()
