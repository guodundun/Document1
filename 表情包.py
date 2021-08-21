import os
import requests
from bs4 import BeautifulSoup
from lxml import etree

class BqbSpider:
    def __init__(self,page):
        # 表情包网站
        self.url = 'https://www.fabiaoqing.com/search/bqb/keyword/%E6%89%93%E6%9E%B6/type/bq/page/{}.html'.format(page)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
        }
        self.path = 'C:/Users/Administrator/Desktop/py_demo/表情包/img/'

    # 获取文件保存到本地
    def get_img(self):

        response = requests.get(self.url).text
        xpath_bds = '//*[@id="bqb"]/div/div/a/img/@data-original'
        xpath_bds1 = '//*[@id="bqb"]/div/div/a/img/@alt'
        html = etree.HTML(response)
        all_url = html.xpath(xpath_bds)
        all_title = html.xpath(xpath_bds1)

        for i in range(len(all_url)):
        #有的图片保存时会报错，所以使用try语句，如果报错，则跳过
            try:
                #保存文件路径及文件名
                with open(self.path + all_title[i] + os.path.splitext(all_url[i])[-1], 'wb') as f:
                    img = requests.get(all_url[i]).content
                    f.write(img)
            except:
                pass

if __name__ == '__main__':

    page = 50
    for i in range(1,page):
        spider = BqbSpider(i)
        spider.get_img()





