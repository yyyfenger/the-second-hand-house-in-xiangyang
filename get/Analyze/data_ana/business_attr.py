import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['axes.unicode_minus'] = False
filename = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\ershoufang-clean-mini-utf8.csv"
names = [
     "id", "communityName", "areaName", "total", "unitPricsValue",
    "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
    "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
    "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
    "fwyt", "fwnx", "cqss", "dyxx", "fbbj"
]
miss_value = ["null", "暂无数据"]
df = pd.read_csv(filename, skiprows=[0], names=names, na_values=miss_value)

# 房屋用途柱状图
count_fwyt = df["fwyt"].value_counts(ascending=True)
count_fwyt.anme = ""
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_xlabel("房源数量(套)")
ax.set_title("襄阳二手房用途水平柱状图", fontsize=18)
count_fwyt.plot(kind="barh")
plt.show()