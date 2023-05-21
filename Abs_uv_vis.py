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
import pandas as pd

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
path_1 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_version1\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_1 = 10
wave_1, epsilon_1 = [],[]
getdata(path_1, wave_1, epsilon_1, nstate_1)

path_2 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_version1\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_2 = 10
wave_2, epsilon_2 = [],[]
getdata(path_2, wave_2, epsilon_2, nstate_2)

path_3 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_version1\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_3 = 10
wave_3, epsilon_3 = [],[]
getdata(path_3, wave_3, epsilon_3, nstate_3)

path_4 = Path('D:\STUDY_think\ALL_Data\\425_G09w-data\Compound_Gv_data\C34H36N2O4\excited_version1\\10-b3lyp-6-311gdp-tzvp-smd\\C34H36N2O4-10-b3lyp-6-311gdp-tzvp-smd_uvvis.txt')
nstate_4 = 10
wave_4, epsilon_4 = [],[]
getdata(path_4, wave_4, epsilon_4, nstate_4)

# 设定浓度
concentration_1 = 0.000007
concentration_2 = 0.000007
concentration_3 = 0.000007
concentration_4 = 0.000007
Abs_epsilon_1 = np.array(epsilon_1)*concentration_1
Abs_epsilon_2 = np.array(epsilon_2)*concentration_2
Abs_epsilon_3 = np.array(epsilon_3)*concentration_3
Abs_epsilon_4 = np.array(epsilon_4)*concentration_4

# 转化为CSV格式
data_1 = pd.DataFrame({'wavelength': wave_1, 'Abs': Abs_epsilon_1})
data_2 = pd.DataFrame({'wavelength': wave_2, 'Abs': Abs_epsilon_2})
data_3 = pd.DataFrame({'wavelength': wave_3, 'Abs': Abs_epsilon_3})
data_4 = pd.DataFrame({'wavelength': wave_4, 'Abs': Abs_epsilon_4})

data = pd.concat([data_1, data_2, data_3, data_4], ignore_index=True).groupby('wavelength', as_index=False).sum()
data.to_csv('D:\STUDY_think\ALL_Data\\425_G09w-data\\python_Abs_fig\\output.csv', index=False)

# 设定绘图阈值
threshold = 1e-1
filtered_data = data[data['Abs'] > threshold]

# 开始绘图
fig = plt.figure(figsize=(8,7))

ax1 = fig.add_subplot(221)
ax1.grid(False)
ax1.patch.set_facecolor('lightgreen')
ax1.patch.set_alpha(0.5)
ax1.set_xlim([0,800])
ax1.set_ylim([0,0.5])
ax1.set_xlabel("wavelenth(nm)")
ax1.set_ylabel('Abs')
# 绘制曲线
ax1.plot(filtered_data['wavelength'], filtered_data['Abs'], color='slateblue', label='Abs', alpha = 0.9)
# ax.plot(data['wavelength'], data['Abs'], color='slateblue', label='Abs', alpha = 0.5)
ax1.legend(loc = "upper right")

ax2 = fig.add_subplot(222)
ax2.grid(False)
ax2.patch.set_facecolor('lightgreen')
ax2.patch.set_alpha(0.5)
ax2.set_xlim([0,800])
ax2.set_ylim([0,0.5])
ax2.set_xlabel("wavelenth(nm)")
ax2.set_ylabel('Abs')
# 绘制曲线
ax2.plot(filtered_data['wavelength'], filtered_data['Abs'], color='slateblue', label='Abs', alpha = 0.9)
# ax.plot(data['wavelength'], data['Abs'], color='slateblue', label='Abs', alpha = 0.5)
ax2.legend(loc = "upper right")

ax3 = fig.add_subplot(223)
ax3.grid(False)
ax3.patch.set_facecolor('lightgreen')
ax3.patch.set_alpha(0.5)
ax3.set_xlim([0,800])
ax3.set_ylim([0,0.5])
ax3.set_xlabel("wavelenth(nm)")
ax3.set_ylabel('Abs')
# 绘制曲线
ax3.plot(filtered_data['wavelength'], filtered_data['Abs'], color='slateblue', label='Abs', alpha = 0.9)
# ax.plot(data['wavelength'], data['Abs'], color='slateblue', label='Abs', alpha = 0.5)
ax3.legend(loc = "upper right")

ax4 = fig.add_subplot(224)
ax4.grid(False)
ax4.patch.set_facecolor('lightgreen')
ax4.patch.set_alpha(0.5)
ax4.set_xlim([0,800])
ax4.set_ylim([0,0.5])
ax4.set_xlabel("wavelenth(nm)")
ax4.set_ylabel('Abs')
# 绘制曲线
ax4.plot(filtered_data['wavelength'], filtered_data['Abs'], color='slateblue', label='Abs', alpha = 0.9)
# ax.plot(data['wavelength'], data['Abs'], color='slateblue', label='Abs', alpha = 0.5)
ax4.legend(loc = "upper right")

plt.show()
