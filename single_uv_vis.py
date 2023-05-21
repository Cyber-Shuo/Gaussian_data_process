import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.collections import LineCollection
from PIL import Image
import numpy as np
from pathlib import Path
import re
import string

# 激发态算了几个就给多少
nstate = 10
number_1 = 10 + nstate
number_2 = 7 + nstate
x_L, y_A, P_X_L, P_Y_V, P_Y2_A = [],[],[],[],[]
img = Image.open('D:\STUDY_think\A_MOST_IMPORTANT\\first-paper\\fig6-1.png')
with open('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_version1\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt','r') as f:
    # 按行读入全部数据
    Alldata = f.readlines()
    # 去除前25行激发态数据存入新列表,如果计算的激发态数目不同则需要修改
    AllSpectradata = Alldata[number_1:]
    # 获取峰值的数据,如果计算的激发态数目不同则需要修改
    Peakdata = Alldata[7:number_2]
    # 为提取去除第一列#的峰值数据新建列表
    PeakdataCut = []
# 提取去除第一列#的峰值数据
for data in Peakdata:
    # 删除数据中的'#'号和空格键
    Cutdata = re.sub(r'[#]','',data)
    # 填入新的峰值数据列表
    PeakdataCut.append('{}'.format(Cutdata))

# 提取全部波长和摩尔吸收系数数据
for Spectradata_data in AllSpectradata:
    value_1 = [float(s) for s in Spectradata_data.split()]
    x_L.append(value_1[0])
    y_A.append(value_1[1])

# 提取特定激发态波长、摩尔吸收系数和振子强度数据
for Peak_data in PeakdataCut:
    value_2 = [float(s) for s in Peak_data.split()]
    P_X_L.append(value_2[0])
    P_Y_V.append(value_2[1])
    P_Y2_A.append(value_2[2])

# 创建图片
fig, ax1 = plt.subplots()
ax1.set_xlim([100,700])
ax1.set_ylim([0,70000])
ax1.set_xlabel("wavelength(nm)")
ax1.set_ylabel('Molar Absorption Coefficient '+r'$\epsilon$')

# 根据衰减长度获取颜色列表
norm = plt.Normalize(100,700)
map_vir = cm.get_cmap(name = 'plasma')
colors = map_vir(norm(x_L))
sm = cm.ScalarMappable(cmap = map_vir, norm = norm)

# 绘制x,y曲线
ps = np.stack((x_L, y_A), axis=1)
segments = np.stack((ps[:-1], ps[1:]), axis=1)
line_segments = LineCollection(segments, colors=colors, linewidths=2, linestyles='solid', cmap = map_vir)
ax1.add_collection(line_segments)
# ax1.plot(x_L, y_A, linewidth = 0.5, color = colors)
ax1.annotate(r'$\lambda$' + '=430nm' + '\n' + r'$\epsilon$' + '=0', xy=(470, 10000), bbox = dict(boxstyle='round', fc='0.95'))

# 绘制第二坐标轴
ax2 = ax1.twinx()
ax2.set_ylim([0,1])
ax2.set_ylabel('Oscillator Strength')
ax2.set_yscale('linear')

# 绘制激发态峰,以振动强度为限制高度
ax2.axvline(x = 0, ymin = 0, ymax = 0, linewidth = 1, color = 'r', label = 'absorb peak')
plt.legend(loc = "upper right")
i = 0
for peak_X in P_X_L:
    peak_Y = P_Y_V[i]
    ax2.axvline(x = peak_X, ymin = 0, ymax = peak_Y, linewidth = 1, color = 'r')
    i += 1

# 画颜色棒
# plt.colorbar(sm, orientation='horizontal')

# 插入图片
ax3 = fig.add_axes([0.6, 0.5, 0.3, 0.3])
ax3.axis('off')
ax3.imshow(img)

# 绘制其他
ax1.fill_between([350,450], 0, 70000, facecolor = 'slateblue', alpha = 0.3)

plt.show()
