import urllib.request
import urllib.parse
import re,bs4
import urllib.request, urllib.parse, http.cookiejar


def getHtml(url):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'),
                         ('Cookie', '4564564564564564565646540')]

    urllib.request.install_opener(opener)

    html_bytes = urllib.request.urlopen(url).read()
    html_string = html_bytes.decode('utf-8')
    return html_string


# url = http://zst.aicai.com/ssq/openInfo/
# 最终输出结果格式如：2015075期开奖号码：6,11,13,19,21,32, 蓝球：4
html = getHtml("http://zst.aicai.com/ssq/openInfo/")
# <table class="fzTab nbt"> </table>

table = html[html.find('<table class="fzTab nbt">'): html.find('</table>')]
# print(table)
# <tr onmouseout="this.style.background=''" onmouseover="this.style.background='#fff7d8'">
# <tr \r\n\t\t                  onmouseout=
tmp = table.split('<tr \r\n\t\t                  onmouseout=', 1)
# str_ssq = re.findall( r'<tr \r\n\t\t’ , table ) #用正则表达式 方法 以后再测试
# print(tmp)
# print(len(tmp))
soup = bs4.BeautifulSoup(table, "lxml")
elems =soup.select('td')
ssq_rqRegex= re.compile(r'20\d\d\d\d\d')
qs_ssq = ssq_rqRegex.findall(str(elems))
print(qs_ssq)

ssq_redRegex= re.compile(r'"redColor sz12">\d+')
redball = ssq_redRegex.findall(str(elems))
# print('redball: \n')
# print(redball)

ssq_redRegex1= re.compile(r'(>\d+)')
redball1 = ssq_redRegex1.findall(str(redball))
# print('redball1: \n')
# print(redball1)

aList = list(redball1)# 直接正则匹配不行？此处存疑
ssq_redRegex2= re.compile(r'(\d+)')
redball2 = ssq_redRegex2.findall(str(aList))
aList2 = list(redball2)# 直接正则匹配不行？此处存疑
print('redball2 遍历: \n')
#for i in aList2:
    #print ("序号：%s   值：%s" % (aList2.index(i) + 1, i), end='')#(redball2.index(i))
    # if i%6==0:
    #     print('')
#上面遍历方式有问题，元素会重复出现，采用新方法
# i =1
for index,Num in enumerate(aList2):
    # i += 1
    if (index+1)%7 ==0 and  index > 0:
        print('一等奖注'+Num)
        continue
    print(str(Num) +' ', end='')#str(i )+' '+str(index)+' ',


# print(aList2)
# print(aList2[0]+aList2[1])

# redball = ssq_redRegex2.findall(str(elems))
# print(qs)
print('处理后的 \n')
# print(redball2)

# print(elems)
trs = tmp[1]
tr = trs[: trs.find('</tr>')]
# print(tr)
# for i in [0,29]:
number = tr.split('<td   >')[1].split('</td>')[0]
print(number + '期开奖号码：', end='')
redtmp = tr.split('<td  class="redColor sz12" >')
reds = redtmp[1:len(redtmp) - 1]  # 去掉第一个和最后一个没用的元素
# print(reds)
for redstr in reds:
    print(redstr.split('</td>')[0] + ",", end='')
print('蓝球：', end='')
blue = tr.split('<td  class="blueColor sz12" >')[1].split('</td>')[0]
print(blue)