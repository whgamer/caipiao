import itchat
import codecs
import json
from pyecharts import Bar,Pie,Map,WordCloud
# 容器类
from collections import Counter
import jieba.analyse

# 数据存储方法，为了防止编码不统一的情况，使用codecs来进行打开
def saveFriends(friendsList):
    outputFile = './result/friends.json'
    with codecs.open(outputFile,'w',encoding='utf-8') as jsonFile:
        # 默认使用ascii，为了输出中文将参数ensure_ascii设置成False
        jsonFile.write(json.dumps(friendsList,ensure_ascii=False))

def getFriends(inputFile):
    with codecs.open(inputFile,encoding='utf-8') as f:
        friendsList = json.load(f)
        return friendsList

# 绘制柱状图
def drawBar(name,rank):
    outputFile = '.\result\省份柱状图.html'
    bar = Bar(title='省份分布柱状图',width=1200,height=600,title_pos='center')
    bar.add(
        '', # 注解label属性
        name, # 横
        rank # 纵
    )
    bar.show_config()
    bar.render(outputFile)

# 绘制饼图
def drawPie(name,rank):
    outputFile = '.\result\性别比例图.html'
    pie = Pie('性别比例图', width=1200, height=600, title_pos='center')
    pie.add(
        '',
        name,rank,
        is_label_show = True, # 是否显示标签
        label_text_color = None, # 标签颜色
        legend_orient = 'vertical', # 图例是否垂直
        legend_pos = 'left'
    )
    pie.render(outputFile)

# 绘制地图
def drawMap(name,rank):
    outputFile = '.\result\区域分布图.html'
    map = Map(title='微信好友区域分布图', width=1200, height=600, title_pos='center')
    map.add(
        '',name,rank,
        maptype = 'china', # 地图范围
        is_visualmap = True, # 是否开启鼠标缩放漫游等
        is_label_show = True # 是否显示地图标记
    )
    map.render(outputFile)

# 绘制个性签名词云
def drawWorldCloud(name,rank):
    outputFile = '.\result\签名词云.html'
    cloud = WordCloud('微信好友签名词云图', width=1200, height=600, title_pos='center')
    cloud.add(
        ' ',name,rank,
        shape='circle',
        background_color='white',
        max_words=200
    )
    cloud.render(outputFile)

# 实现将counter数据结构拆分成两个list，再传给pyecharts
def counter2list(_counter):
    nameList,countList = [],[]
    for counter in _counter:
        nameList.append(counter[0])
        countList.append(counter[1])
    return nameList,countList

def  dict2list(_dict):
    nameList, countList = [], []
    for key,value in _dict.items():
        nameList.append(key)
        countList.append(value)
    return nameList, countList

# 利用jieba模块提取出关键词并计算其权重，利用了TF-IDF算法
def extractTag(text,tagsList):
    if text:
        tags = jieba.analyse.extract_tags(text)

        for tag in tags:
            tagsList[tag] += 1

if __name__ == '__main__':
    # 性别在itchat接口获取的数据中显示的是0，1，2三种我们使用一个字典将其映射为男、女、其他
    sexList = {'0': '其他', '1': '男', '2': '女'}
    # 自动登陆
    itchat.auto_login()
    # 利用API获取朋友列表
    friends = itchat.get_friends(update=True)

    friendsList = []
    for friend in friends:
        # 将friends提取出有用数据并存放在字典中
        item = {}
        item['NickName'] = friend['NickName']
        item['Sex'] = sexList[str(friend['Sex'])]
        item['Province'] = friend['Province']
        item['Signature'] = friend['Signature']
        # 为了获取头像用
        item['UserName'] = friend['UserName']

        friendsList.append(item)

    # 保存好友列表的json信息
    saveFriends(friendsList)

    # 读取friends.json中的数据
    inputFile = '.\result\friends.json'
    friendList = getFriends(inputFile)

    # 需要统计的字段使用counter数据类型存储
    provinceCounter = Counter()
    sexDict = {'男':0,'女':0,'其他':0}
    signatureCounter = Counter()

    for friend in friendList:
        if friend['Province']  != '':
            provinceCounter[friend['Province']] += 1
        sexDict[friend['Sex']] += 1
        extractTag(friend['Signature'],signatureCounter)

    # 统计出排名前16的省份
    provinceList,rankList = counter2list(provinceCounter.most_common(15))
    # 绘制柱状图
    drawBar(provinceList, rankList)

    # 绘制地图
    drawMap(provinceList, rankList)

    # 绘制男女比例饼图
    sexList,percentList = dict2list(sexDict)
    drawPie(sexList, percentList)

    # 绘制词云
    tagsList,rankList = counter2list(signatureCounter.most_common(200))
    drawWorldCloud(tagsList, rankList)