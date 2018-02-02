#python3
import requests,bs4
import urllib.request,urllib3
# res =requests.get('http://caipiao.163.com/award/ssq/2018006.html')
# res.raise_for_status()
# caiPiaoSoup =bs4.BeautifulSoup(res.text,"html")
#
# exampleFile= open('example.html')
# exampleSoup =bs4.BeautifulSoup(exampleFile.read())
# elems =exampleSoup.select('p #zj_area')
# print(elems)
from urllib import request
def getHtml(url):  #获取页面的源代码
    # page= urllib.urlopen(url)
    res =requests.get('http://caipiao.163.com/award/ssq/2018006.html')
    res.raise_for_status()
    print('res '+str(res))
    caiPiaoSoup =bs4.BeautifulSoup(res,"html.parser")

    page = request.urlopen(url)
    print(caiPiaoSoup)
    html = page.read()
    print('html'+str(html))
    html = html.decode('utf-8')
    return html
print(getHtml('http://caipiao.163.com/award/ssq/2018006.html'))

from urllib import request
import gzip
def getHtml(url):  #获取页面的源代码
    page = request.urlopen(url)
    html = page.read()
    html = gzip.decompress(html)
    html = html.decode('utf-8')
    return html
print(getHtml('http://caipiao.163.com/award/ssq/2018006.html'))

def getball(html): #正则匹配出开奖号码
    regall = r'<p id="zj_area">(.+)</p>'
    reg = r'<span class="red_ball">([0-9])</span>'
    balllist = reg.findall(regall,html)
    openball = reg.findall(reg,balllist[0])
    return openball
def insertTxt(file,data): #将开奖号码保存到文件中
    in_put = open(file, 'w')
    in_put.write(str(data))
    in_put.close()
def getTxt(file): #从文件中读取之前的开奖号码
    out_put = open(file, 'r')
    result = out_put.read()
    out_put.close()
    return result
# 在下面的代码中我把发邮件的逻辑直接写进去了，这里我隐藏了邮件的相关信息，同时也不讲解发邮件的相关内容，有兴趣的可以自己去研究，使用的是python自带的smtp库。
def deal(url): #主逻辑
    html = getHtml(url)
    openball = str(getball(html)) #将开奖的list转换成str
    oldball = getTxt('data.txt') #从文件中读取历史开奖号码
    if openball==oldball:
        print('还没开奖')
    else:
        insertTxt('data.txt',openball)  #更新开奖号码保存文件

        mail_host=""  #设置服务器
        mail_user=""    #用户名
        mail_pass=""   #口令

        # message = MIMEText('本期七星彩开奖结果'+openball, 'plain', 'utf-8')
        # message['From'] = Header("python系统", 'utf-8')
        # message['To'] =  Header("", 'utf-8')
        # subject = '七星彩开奖结果'
        # message['Subject'] = Header(subject, 'utf-8')
        #
        # smtpObj = smtplib.SMTP()
        # smtpObj.connect(mail_host, 25)
        # smtpObj.login(mail_user,mail_pass)
        # smtpObj.sendmail('','', message.as_string())
        # print('和上次号码不同，已开奖')
        print(openball)
