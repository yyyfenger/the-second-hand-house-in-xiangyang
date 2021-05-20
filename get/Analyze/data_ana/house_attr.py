import numpy as np
# import matplotlib.use('TkAgg')
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import pandas as pd

# plt .rcParams['font.family'] = 'YaHei Consolas Hybrid'
# plt .rcParams['fon.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据加载
filename = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\ershoufang-clean-mini-utf8.csv"
names = [
    "id", "communityName", "areaName", "total", "unitPricsValue",
    "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
    "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
    "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
    "fwyt", "fwnx", "cqss", "dyxx", "fbbj"
]
miss_value = ["null", "暂无数据"]
df = pd.read_csv(filename, encoding="utf-8", skiprows=[0], names=names, na_values=miss_value)

# # 户型占比
# count_fwhx = df["fwhx"].value_counts()[:10]
# count_other_fwhx = pd.Series({"其他": df["fwhx"].value_counts()[10:].count()})
# count_fwhx = count_fwhx.append(count_other_fwhx)
# count_fwhx.index.name = ""
# count_fwhx.name = ""
# fig = plt.figure(figsize=(9, 9))
# ax = fig.add_subplot(111)
# ax.set_title("襄阳二手房户型占比情况", fontsize=18)
# # colors = cm.rainbow(np.linspace(0, 1, 10))
# colors = ['red','yellowgreen','lightskyblue']
# count_fwhx.plot(kind="pie", autopct="%3.1f%%", fontsize=12)

#
# sizes = [60, 30, 10]
# explode = (0.05, 0, 0)
# colors = ['r', 'g', 'y', 'b']
# patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,  labeldistance = 1.1,autopct = '%3.1f%%',shadow = False, startangle = 90, pctdistance = 0.6)

# # 房屋装修
# count_zxqk = df["zxqk"].value_counts()
# count_zxqk.name = ""
# fig = plt.figure(figsize=(9, 9))
# ax = fig.add_subplot(111)
# ax.set_title("襄阳二手房装修占比情况", fontsize=18)
# count_zxqk.plot(kind="pie", autopct="%3.1f%%", fontsize=12)
#
# # 建筑类型
# count_jzlx = df["jzlx"].value_counts()
# count_jzlx.name = ""
# fig = plt.figure(figsize=(9, 9))
# ax = fig.add_subplot(111)
# ax.set_title("襄阳二手房建筑类型占比情况", fontsize=18)
# count_jzlx.plot(kind="pie", autopct="%3.1f%%", fontsize=12)
# # plt.text(1, -1.2, "建筑二手房占比类型", fontsize=12)
# plt.show()

# 房屋朝向
count_fwcx = df["fwcx"].value_counts()[:15]
count_other_fwcx = pd.Series({"其他": df["fwcx"].value_counts()[15:].count()})
count_fwcx =count_fwcx.append(count_other_fwcx)
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_title("襄阳二手房朝向分布情况", fontsize=18)
count_fwcx.plot(kind="bar", fontsize=12)

# 建筑面积分布区间
area_level = [0, 50, 100, 150, 200, 250, 300, 500]
label_level = ["小于50", "50-100", "100-150", "150-200", "200-250", "250-300", "300-350"]
jzmj_cut = pd.cut(df["jzmj"], area_level, labels=label_level)
jzmj_result = jzmj_cut.value_counts()
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_ylabel("建筑面积(㎡)")
ax.set_title("襄阳二手房建筑面积分布区间", fontsize=18)
jzmj_result.plot(kind="barh", fontsize=12)

plt.show()