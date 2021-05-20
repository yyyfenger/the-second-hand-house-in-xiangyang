import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

filename = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\ershoufang-clean-mini-utf8.csv"
names = [
    "id", "communityName", "areaName", "total","unitPriceValue",
        "fwhx", "szlc", "jzmj", "hxjg", "tnmj",
        "jzlx", "fwcx", "jzjg", "zxqk", "thbl",
        "pbdt", "cqnx", "gpsj", "jyqs", "scjy",
        "fwyt", "fwnx", "cqss", "dyxx", "fbbj",
          ]
miss_value = ["null", "暂无数据"]
df = pd.read_csv(filename, skiprows=[0], names=names, na_values=miss_value)

# 1、平均单价
groups_unitprice_area = df["unitPriceValue"].groupby(df["areaName"])
mean_uniprice = groups_unitprice_area.mean()
mean_uniprice.index.name = ""
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_ylabel("单价(元/平米)", fontsize=12)
ax.set_title("襄阳二手房平均单价", fontsize=18)
mean_uniprice.plot(kind="bar", fontsize=12)

# # 2、总价箱线图
# box_total_area = df["total"].groupby(df["areaName"])
# box_data = pd.DataFrame(list(range(21000)))
# for name, group in box_total_area:
#     box_data[name] = group
# del box_data["start"]
# fig = plt.figure(figsize=(12, 7))
# ax = fig.add_subplot(111)
# ax.set_ylabel("总价(万元)", fontsize=14)
# ax.set_title("襄阳二手房总价箱线图", fontsize=18)
# box_data.plot(kind="box", fontsize=12, sym="r+", grid=True, ax=ax, yticks=[0, 200, 500, 1000, 2000, 3000], ylim=[0, 2100])
#
# 3、平均建筑面积
groups_area_jzmj = df["jzmj"].groupby(df["areaName"])
mean_jzmj = groups_area_jzmj.mean()
mean_jzmj.index.name = ""
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_ylabel("建筑面积(㎡)", fontsize=14)
ax.set_title("襄阳二手房平均建筑面积", fontsize=18)
mean_jzmj.plot(kind="bar", fontsize=12)

# 4、平均单价和平均建筑面积
groups_uniprice_erea = df["unitPriceValue"].groupby(df["areaName"])
mean_uniprice = groups_unitprice_area.mean()
mean_uniprice.index.name = ""
groups_unitprice_jzmj = df["jzmj"].groupby(df["areaName"])
mean_jzmj = groups_area_jzmj.mean()
mean_jzmj.index.name = ""
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax1.set_ylabel("单价(元/平米)", fontsize=14)
ax1.set_title("襄阳二手当平均单价", fontsize=18)
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_ylabel("建筑面积(㎡)", fontsize=14)
ax2.set_title("襄阳二手房平均建筑面积", fontsize=18)
plt.subplots_adjust(hspace=0.4)
mean_uniprice.plot(kind="bar", ax=ax1, fontsize=12)
mean_jzmj.plot(kind="bar", ax=ax2, fontsize=12)

# 5、房源数量
groups_area = df["id"].groupby(df["areaName"])
count_area = groups_area.count()
count_area.index.name = ""
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_ylabel("房源数量(套)", fontsize=14)
ax.set_title("襄阳二手房房源数量", fontsize=18)
count_area.sort_values().plot(kind="line", fontsize=12, grid=True, marker="o")

# 6、二手房单价最高top20
unitprice_top = df.sort_values(by="unitPriceValue", ascending=False)[:20]
unitprice_top = unitprice_top.sort_values(by="unitPriceValue")
unitprice_top.set_index(unitprice_top["communityName"], inplace=True)
unitprice_top.index.name = ""
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_ylabel("单价(元/平方)", fontsize=14)
ax.set_title("襄阳二手房单价最高top20", fontsize=18)
unitprice_top["unitPriceValue"].plot(kind="barh", fontsize=12)

# 7、二手房总价与建筑面积散点图
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_title("襄阳二手房总价与建筑面积散点图", fontsize=18)
df.plot(x="jzmj", y="total", kind="scatter", fontsize=12, ax=ax, alpha=0.4, xticks=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700], xlim=[0, 800])
ax.set_xlabel("建筑面积(㎡)", fontsize=14)
ax.set_ylabel("总价(万元)", fontsize=14)

# 8、二手房单价与建筑面积散点图
fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(111)
ax.set_title("襄阳二手房单价与建筑面积散点图", fontsize=18)
df.plot(x="jzmj", y="unitPriceValue", kind="scatter", grid=True,fontsize=12, ax=ax, alpha=0.4, xticks=[0, 50, 100, 150, 200, 250, 300, 400, 500, 600, 700], xlim=[0, 800])
ax.set_xlabel("建筑面积(㎡)", fontsize=14)
ax.set_ylabel("单价(元/平米)", fontsize=14)


plt.show()