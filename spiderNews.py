#python3
import scrapy
import hashlib
from tutorial.items  import JinLuoSiItem
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector

class WsjSpider (scrapy.spiders.Spider):
    count = 0
    url_set = set()
    name ="spiderNews"
    domain ='http://www.whws.gov.cn/col/col29396/index.html'#爬取威海卫计委通知信息 add by zyy 2018年2月7日
    allowed_domains =["whws.gov.cn"]
    start_urls = ["http://www.whws.gov.cn/col/col29396/index.html"]

    def parse(self,reponse):
        md5_obj =hashlib.md5()
        md5_obj.update(reponse.url)
        md5_url =md5_obj.hexdigest()
        if md5_url in WsjSpider.url_set:
            pass
        else:
            WsjSpider.url_set.add(md5_url)
            hxs =HtmlXPathSelector(reponse)
            if reponse.url.startswith('http://www.whws.gov.cn/col/col29396/index.html'):
                item[]=;