from Get.download import HtmlDownloader
from Get.outputer import HtmlOutputer
from Get.parser import HtmlParser
from Get.url_manager import UrlManager
from Get.log import MyLog


class Main():
    def __init__(self):
        self.urls = UrlManager()
        self.log = MyLog("main", "logs")
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()
        # self.util=utill.DBConn()

    def craw(self, root_url):
        # areas = {
        #     "xiangchengqu1": 2724, "xaingzhouqu1": 3513, "fanchengqu": 7333
        # }
        # areas = {
        #      "xaingzhouqu1": 3513
        # }
        areas = {
            "fanchengqu": 7333
        }
        # 1、抓详情链接
        for area, pg_sum in areas.items():
            for num in range(1, pg_sum + 1):
                # 1.1拼接页面
                pg_url = root_url + area + "/pg" +  str(num) + "/"
                self.log.logger.info("1.1拼页地址" + pg_url)
                print("1.1拼页地址" + pg_url)
                # 1.2下载页面
                try:
                    html_cont = self.downloader.download(pg_url)
                except Exception as e:
                    self.log.logger.error("1.2 下载页面出现异常:" + repr(e))
                    # time.sleep(60 * 30)
                else:
                    # 1.3解析详情页面
                    try:
                        ershoufang_urls = self.parser.get_ershoufang_urls(html_cont)

                    except Exception as e:
                        self.log.logger.error("1.3 页面解析出现异常:" + repr(e))
                    else:
                        self.urls.add_new_urls(ershoufang_urls)
        # 2.1获取详细页面
        id = 1
        # stop = 1
        while self.urls.has_new_url():
            # 2.1 获取url
            try:
                detail_url = self.urls.get_new_url()
                self.log.logger.info("2.1地址" + detail_url)
                print("2.1地址" + detail_url)
            except Exception as e:
                print("2.1拼接地址异常")
                self.log.logger.error("2.1拼接地址异常" + detail_url)
            # 2.2下载页面
            try:
                detail_html = self.downloader.download(detail_url)
            except Exception as e:
                self.log.logger.error("2.2 下载页面异常" + repr(e))
                self.urls.add_new_url(detail_url)
            else:
                # 2.3解析页面
                try:
                    ershoufang_data = self.parser.get_ershoufang_data(detail_html, id)
                except Exception as e:
                    self.log.logger.error("2.3解析异常" + repr(e))
                else:
                    # 2.4 输出数据
                    try:
                        self.outputer.collect_data(ershoufang_data)
                    except Exception as e:
                        self.log.logger.error("2.4输出异常" + repr(e))
                    else:
                        print(id)
                        id = id + 1
                        # stop = stop + 1
                        # if stop == 2500:
                        #     stop = 1
                            # time.sleep(60 * 20)



if __name__ == "__main__":
    root_url = "https://xy.lianjia.com/ershoufang/"
    obj_spider = Main()
    obj_spider.craw(root_url)

