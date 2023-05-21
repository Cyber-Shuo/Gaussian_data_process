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
path_1 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_1 = 10
wave_1, epsilon_1 = [],[]
getdata(path_1, wave_1, epsilon_1, nstate_1)

path_2 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\10-b3lyp-tzvp-tzvp-smd\\C34H36N2O4-10-b3lyp-tzvp-tzvp-smd_uvvis.txt')
nstate_2 = 10
wave_2, epsilon_2 = [],[]
getdata(path_2, wave_2, epsilon_2, nstate_2)

path_3 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\10-pbe0-tzvp-tzvp-pcm\\C34H36N2O4-10-pbe0-tzvp-tzvp-pcm_uvvis.txt')
nstate_3 = 10
wave_3, epsilon_3 = [],[]
getdata(path_3, wave_3, epsilon_3, nstate_3)

path_4 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\10-pbe0-tzvp-tzvp-smd\\C34H36N2O4-10-pbe0-tzvp-tzvp-smd_uvvis.txt')
nstate_4 = 10
wave_4, epsilon_4 = [],[]
getdata(path_4, wave_4, epsilon_4, nstate_4)

path_5 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\10-pbe0-tzvp-2tzvp-smd\\C34H36N2O4-10-pbe0-tzvp-2tzvp-smd_uvvis.txt')
nstate_5 = 10
wave_5, epsilon_5 = [],[]
getdata(path_5, wave_5, epsilon_5, nstate_5)

path_6 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\30-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-30-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_6 = 30
wave_6, epsilon_6 = [],[]
getdata(path_6, wave_6, epsilon_6, nstate_6)

path_7 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\30-b3lyp-tzvp-tzvp-smd\\C34H36N2O4-30-b3lyp-tzvp-tzvp-smd_uvvis.txt')
nstate_7 = 30
wave_7, epsilon_7 = [],[]
getdata(path_7, wave_7, epsilon_7, nstate_7)

path_8 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\30-pbe0-tzvp-tzvp-pcm\\C34H36N2O4-30-pbe0-tzvp-tzvp-pcm_uvvis.txt')
nstate_8 = 30
wave_8, epsilon_8 = [],[]
getdata(path_8, wave_8, epsilon_8, nstate_8)

path_9 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_state_verify_version1\\30-pbe0-tzvp-tzvp-smd\\C34H36N2O4-30-pbe0-tzvp-tzvp-smd_uvvis.txt')
nstate_9 = 30
wave_9, epsilon_9 = [],[]
getdata(path_9, wave_9, epsilon_9, nstate_9)


# 开始绘图
fig,ax = plt.subplots(figsize=(8, 6))
ax.grid(False)
ax.set_xlim([100,800])
ax.set_ylim([0,80000])
ax.set_xlabel("wavelength(nm)")
ax.set_ylabel('Molar Absorption Coefficient ' + r'$\epsilon$')

ax2 = fig.add_axes([0.35, 0.7, 0.15, 0.15])
ax2.set_xlim([240,280])
ax2.set_ylim([60000,75000])
ax2.set_yticklabels(['6W','6.5W','7W','7.5W'])

ax3 = fig.add_axes([0.5, 0.23, 0.3, 0.3])
ax3.set_xlim([260,320])
ax3.set_ylim([10000,20000])

# 绘制曲线
ax.plot(wave_1, epsilon_1, color='red', alpha = 0.7, label='10/B3LYP/6-311g(d,p)/def-TZVP/SMD')
ax.plot(wave_2, epsilon_2, color='blue', alpha = 0.7, label='10/B3LYP/def-TZVP/def-TZVP/SMD')
ax.plot(wave_3, epsilon_3, color='green', alpha = 0.7, label='10/PBE0/def-TZVP/def-TZVP/IEFPCM')
ax.plot(wave_4, epsilon_4, color='yellow', alpha = 0.7, label='10/PBE0/def-TZVP/def-TZVP/SMD')
ax.plot(wave_5, epsilon_5, color='pink', alpha = 1, label='10/PBE0/def-TZVP/def2-TZVP/SMD')
ax.plot(wave_6, epsilon_6, color='cyan', alpha = 0.7, label='30/B3LYP/6-311g(d,p)/def-TZVP/SMD')
ax.plot(wave_7, epsilon_7, color='maroon', alpha = 0.7, label='30/B3LYP/def-TZVP/def-TZVP/SMD')
ax.plot(wave_8, epsilon_8, color='black', alpha = 0.7, label='30/PBE0/def-TZVP/def-TZVP/IEFPCM')
ax.plot(wave_9, epsilon_9, color='orange', alpha = 0.7, label='30/PBE0/def-TZVP/def-TZVP/SMD')

ax2.plot(wave_6, epsilon_6, color='cyan', alpha = 0.7, label='30/B3LYP/6-311g(d,p)/SMD')
ax2.plot(wave_7, epsilon_7, color='maroon', alpha = 0.7, label='30/B3LYP/def-TZVP/SMD')
ax2.plot(wave_8, epsilon_8, color='black', alpha = 0.7, label='30/PBE0/def-TZVP/IEFPCM')
ax2.plot(wave_9, epsilon_9, color='orange', alpha = 0.7, label='30/PBE0/def-TZVP/SMD')

ax3.plot(wave_3, epsilon_3, color='green', alpha = 0.7, label='10/PBE0/def-TZVP/def-TZVP/IEFPCM')
ax3.plot(wave_4, epsilon_4, color='yellow', alpha = 0.7, label='10/PBE0/def-TZVP/def-TZVP/SMD')
ax3.plot(wave_5, epsilon_5, color='pink', alpha = 1, label='10/PBE0/def-TZVP/def2-TZVP/SMD')

ax.legend(loc = "upper right")
plt.show()
