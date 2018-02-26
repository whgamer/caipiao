import urllib.request
import urllib.parse
import requests
import re,bs4
import urllib.request, urllib.parse, http.cookiejar
from collections import Counter


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2015-10-09 13:51:35
# Project: xinwen
#http://demo.pyspider.org/debug/xinwen

from pyspider.libs.base_handler import *

import re

class Handler(BaseHandler):
    crawl_config = {
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://www.gov.cn/xinwen/', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            matchObj = re.match( r'(.*).htm', each.attr.href, re.M|re.I)
            if matchObj:
                self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "http-equiv":response.doc('meta').attr('http-equiv'),
            "keywords":response.doc('meta[name="keywords"]').attr('content'),
        }
# test =Handler()
# test.on_start()
#!/usr/bin/env python3
# from urllib import request
#
# USER_AGENT = r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36'
#
# req = request.Request(r'http://www.whws.gov.cn/col/col29396/index.html', headers={'User-Agent': USER_AGENT, 'Accept-Encoding': 'gzip'})
# res = request.urlopen(req)
#
# print(res.info().get('Content-Encoding'))
# def getHtml(url):
#     cj = http.cookiejar.CookieJar()
#     opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
#     # opener.add_header('Accept-encoding', 'gzip')
#     opener.addheaders = [('User-Agent',
#                           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
#                          ('Cookie', '4564564564564564565646540')]
#     urllib.request.install_opener(opener)
#     html_bytes = urllib.request.urlopen(url).read()
#     html_string = html_bytes.decode('utf-8')
#     return html_string
#
#
# # import urllib2, httplib
#
#
# html = getHtml("http://www.whws.gov.cn/col/col29396/index.html")
# # <table class="fzTab nbt"> </table>
# requests.add_header('Accept-encoding', 'gzip')
# res =requests.get('http://www.whws.gov.cn/module/visitcount/visit.jsp?type=2&i_webid=91&i_columnid=29396')
# # table1 = html[0:]
# # table = html[html.find('<div id="List1"'): html.find('</table></div>')]
#
# opener = build_opener()
# f = opener.open(request)
# wsj = bs4.BeautifulSoup(res.text,"lxml")
# elems =wsj.select('div')
# print(elems)


