# coding:utf-8
# import HTMLParser
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import requests,bs4
import re
import cgi
import html


url = 'http://www.whws.gov.cn/col/col29396/index.html'

#获得网页源码
data = requests.get(url)
data.encoding='utf-8' #显式地指定网页编码，一般情况可以不用
# print(data.text)
#图片正则表达式
regex = r'(CDATA[)(.*]]&)'

#re是一个列表
# pa = re.compile(regex) #创建一个pa模板，使其符合匹配的网址
wzSoup =bs4.BeautifulSoup(data.text,"html.parser")
wzIndex = wzSoup.select('#List1')
# print(wzIndex[0])
s=str(wzIndex[0].text)
s = s.replace("&lt;", "<")
print(s)
str =html.escape(wzIndex[0].text,'')
Elems =bs4.BeautifulSoup(wzIndex[0].text,"html.parser")
webSite =Elems.select('title')




my_sender='xiao..ao@163.com'    # 发件人邮箱账号
my_pass = '55girl'              # 发件人邮箱密码(当时申请smtp给的口令)
my_user='xiao..ao@163.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
        msg['From']=formataddr(["发件人昵称",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["收件人昵称",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题

        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

# print(webSite[0].text)
# ma = re.findall(regex,data.text) #findall 方法找到data中所有的符合pa的对象，添加到re中并返回
# print(ma)
#图片的名字
# i=0

#要在控制台打印提示，了解进程
# print('Start downloading')

#将ma中图片网址依次提取出来
# for image in ma:
#     i+=1
#     image = requests.get(image).content
#     print(str(i)+'.jpg is downloading')
#
#     # \ 要用转义符号 \\表示，要注意原图片的格式
#     with open('D:\Python Study\crawl\crawl pictures\\'+str(i)+'.jpg','wb') as f: #注意打开的是就jpg文件
#          f.write(image)

# print('Finish downloading')