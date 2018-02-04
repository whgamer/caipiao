import urllib.request
import urllib.parse
import re,bs4
import urllib.request, urllib.parse, http.cookiejar
from collections import Counter

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

#获取篮球
def getBuleBall(elems):
    ssq_blueRegex = re.compile(r'"blueColor sz12">\d+')
    blueball = ssq_blueRegex.findall(str(elems))
    blueball1 = []
    for num_blue in blueball:
        blueball1.append(num_blue[-2:])
    return blueball1
#获取红球
def getRedBall(elems):
    ssq_redRegex = re.compile(r'"redColor sz12">\d+')
    redball = ssq_redRegex.findall(str(elems))
    ssq_redRegex1 = re.compile(r'(>\d+)')
    redball1 = ssq_redRegex1.findall(str(redball))
    aList = list(redball1)  # 直接正则匹配不行？此处存疑
    ssq_redRegex2 = re.compile(r'(\d+)')
    redball2 = ssq_redRegex2.findall(str(aList))
    aList2 = list(redball2)  # 直接正则匹配不行？此处存疑
    # print('redball2 遍历: \n')
    list_redhm = []  # 添加保存篮球号码
    for index, Num in enumerate(aList2):
        # i += 1
        if (index + 1) % 7 == 0 and index > 0:
            # print('一等奖注' + Num)
            continue
        # print(str(Num) + ' ', end='')  # str(i )+' '+str(index)+' ',
        list_redhm.append(Num)
    # print(list_redhm)
    return list_redhm
#获取前几位号码
def getCountNum(count,list_redhm,list_bluehm):
    num_count = Counter(list_redhm)
    num_count_red = num_count.most_common(count)

    print('红球前六位（根据最近30期）')
    print(num_count_red)
    num_count = Counter(list_bluehm)
    num_count_blue = num_count.most_common(count)
    print('蓝球前六位（根据最近30期）')
    print(num_count_blue)
#获取彩票期数
def getQs(elems):
    ssq_rqRegex = re.compile(r'20\d\d\d\d\d')
    qs_ssq = ssq_rqRegex.findall(str(elems))
    print(qs_ssq)
#获取最近一期号码
def getLastLottery():
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
getCountNum(6,getBuleBall(elems),getRedBall(elems))

dict_ssq ={'qs':'','redball':'','buleball':'','ydj':''}#创建一个字典存放双色球信息


