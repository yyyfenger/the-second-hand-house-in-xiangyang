from bs4 import BeautifulSoup
import requests
import re

import urllib3

class test:
    def __init__(self):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Host": "nj.lianjia.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
        }

    def getdata(self):
        # url = "https://nj.lianjia.com/ershoufang/103110876240.html"
        # self.url = 'https://nj.lianjia.com/ershoufang/gulou/'

        # r = requests.get(self.url, headers= self.headers)

        # ershoufang_data = []
        # communityName = "null"
        # ereaName = "null"
        # total = "null"
        # unitPriceValue = "null"

        r = open("11.html", "rb")
        bsObj = BeautifulSoup(r, "html.parser")

        # with open("11.html", "w", encoding='utf-8') as file:
        #     file.write(r.text)

        # 小区名称
        # tag_com = bsObj.select("#content > div.leftContent > ul > li:nth-child(1) > div.info.clear > div.flood > div > a:nth-child(2)")
        # tag_com = bsObj.select("#introduction > div > div > div.transaction > div.content > ul > li:nth-child(1) > span:nth-child(2)")

        all_area = bsObj.findAll("div", {"class": "positionInfo"})
        # all_urls = bsObj.findAll("div", {"class": "title"})

        if all_area is None:
            print("..........")
        else:
            # print(all_area.get_text())
            id = 0
            for name in all_area:
                id += 1
                # print(name.get_text() + str(id))
                # pattern = r'(.*?)\s[4]\-'
                print(name.get_text())
                area = re.search(r'^(.*?)\s', name, re.S)
                tag_com = re.search(r'-\s*(.*?)\s*$', name, re.S)
                # print(area.group(0))
                # print(tag_com.group(1))


            # print(tag_com.get_text)

if __name__ == "__main__":
    get = test()
    get.getdata()