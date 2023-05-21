import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.collections import LineCollection
from PIL import Image
import numpy as np
from pathlib import Path
import re
import string
from mpl_toolkits.mplot3d.art3d import Line3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# 获取数据函数
def getdata(path, wave, epsilon, nstate):
    number_1 = 10 + nstate
    with open(path,'r') as f:
        Alldata = f.readlines()
        AllSpectradata = Alldata[number_1:]
    for Spectradata_data in AllSpectradata:
        value_1 = [float(s) for s in Spectradata_data.split()]
        wave.append(value_1[0])
        epsilon.append(value_1[1])  

# 设定绘制的文件
path_1 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\excited_state_verify\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_1 = 10
wave_1, epsilon_1 = [],[]
getdata(path_1, wave_1, epsilon_1, nstate_1)

path_2 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\excited_state_verify\\30-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-30-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_2 = 30
wave_2, epsilon_2 = [],[]
getdata(path_2, wave_2, epsilon_2, nstate_2)

# 开始绘图
fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
# ax.zaxis.pane.fill = False

ax.set_xlim([100,800])
ax.set_ylim([0,100])
ax.set_zlim([0,80000])

ax.set_xlabel("wavelenth(nm)")
# ax.set_ylabel('compound name')
ax.set_zlabel('Molar Absorption Coefficient ' + r'$\epsilon$')

# 绘制曲线并填充渐变色
ax.plot(wave_1, epsilon_1, zs=0, zdir='y', color='r', label='10/B3LYP/6-311g(d,p)/SMD')
loc_list_1 = []
for i in range(0, len(wave_1)):
    loc = 0
    loc_list_1.append(loc)
for i in range(1, len(epsilon_1)):
    vertices = [[(wave_1[i-1], loc_list_1[i-1], epsilon_1[i-1]), (wave_1[i], loc_list_1[i], epsilon_1[i]), (wave_1[i], loc_list_1[i], 0), (wave_1[i-1], loc_list_1[i-1], 0)]]
    color = plt.cm.inferno((wave_1[i] - np.min(wave_1)) / (np.max(wave_1) - np.min(wave_1)))
    poly = Poly3DCollection(vertices, facecolors=color)
    ax.add_collection3d(poly)
# 简单填充
# vertices_1 = [list(zip(loc_list_1, wave_1, epsilon_1))]
# poly_1 = Poly3DCollection(vertices_1, alpha=0.5, facecolor='red')
# ax.add_collection3d(poly_1)

ax.plot(wave_2, epsilon_2, zs=20, zdir='y', color='b', label='30/B3LYP/6-311g(d,p)/SMD')
loc_list_2 = []
for i in range(0, len(wave_2)):
    loc = 20
    loc_list_2.append(loc)
for i in range(1, len(epsilon_2)):
    vertices = [[(wave_2[i-1], loc_list_2[i-1], epsilon_2[i-1]), (wave_2[i], loc_list_2[i], epsilon_2[i]), (wave_2[i], loc_list_2[i], 0), (wave_2[i-1], loc_list_2[i-1], 0)]]
    color = plt.cm.winter((wave_2[i] - np.min(wave_2)) / (np.max(wave_2) - np.min(wave_2)))
    poly = Poly3DCollection(vertices, facecolor=color)
    ax.add_collection3d(poly)

ytick_labels = ['20', '21']
ax.set_yticklabels(ytick_labels, rotation = -60)

ax.view_init(elev=15, azim=-60)
plt.legend(loc = "upper right")
plt.show()
