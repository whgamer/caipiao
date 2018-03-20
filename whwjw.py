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
mailto_list=['touser@qq.com']           #收件人(列表)
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="fromuser@163.com"                           #用户名
mail_pass="password"                             #密码
mail_postfix="163.com"

#获得网页源码
def getdata(url):
    data = requests.get(url)
    data.encoding='utf-8' #显式地指定网页编码，一般情况可以不用


    #re是一个列表
    # pa = re.compile(regex) #创建一个pa模板，使其符合匹配的网址
    wzSoup =bs4.BeautifulSoup(data.text,"html.parser")
    wzIndex = wzSoup.select('#List1')
    # print(wzIndex[0])
    s=str(wzIndex[0].text)
    s = s.replace("&lt;", "<")
    # print(s)
    # str =html.escape(wzIndex[0].text,'')
    # Elems =bs4.BeautifulSoup(wzIndex[0].text,"html.parser")
    # webSite =Elems.select('title')
    #图片正则表达式
    pattern_title = r"bt_link' title='(.*?)' target="
    pattern_href = r"<a  style=\"font-size:14px;\" href='(.*?)'"
    pattern_date = r'class=\"bt_time\" style=\"font-size:14px;border-bottom:dashed 1px #ccc">\[(.*?)\]'
    # pa = re.compile(regex)
    title = re.findall(pattern_title,s)
    href = re.findall(pattern_href,s)# return a list
    date = re.findall(pattern_date,s)

    for (str_title ,str_href,str_date) in zip(title,href,date):
        # print(str_date+'   '+ str_title +' \n  '+'http://www.whws.gov.cn'+str_href)
        for i in range(1):  # 发送1封，上面的列表是几个人，这个就填几
            if send_mail(mailto_list,  str_title, str_date+'   '+ str_title +'  \n '+'http://www.whws.gov.cn'+str_href):  # 邮件主题和邮件内容\n change row  \r enter
                # 这是最好写点中文，如果随便写，可能会被网易当做垃圾邮件退信
                print(str_title+str_date+"邮件发送成功!")
            else:
                print("发送失败!")
# print(len(title))# return list elements count
# print(len(href))
# print(len(date))



                  #邮箱的后缀，网易就是163.com
def send_mail(to_list,sub,content):
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)                            #连接服务器
        server.login(mail_user,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception:
        # print str(e)
        return False
if __name__ == '__main__':
    pt = getdata(url)
