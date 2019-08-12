import itchat
import pandas as pd
import matplotlib.pyplot as plt
import csv
from collections import Counter

from pyecharts import Geo, Bar



itchat.login()
friends = itchat.get_friends(update=True)[0:]

def analyseSex(firends):
    sexs = list(map(lambda x:x['Sex'],friends[1:]))
    counts = list(map(lambda x:x[1],Counter(sexs).items()))
    labels = ['Male','Female','Unknow']
    colors = ['red','yellowgreen','lightskyblue']
    plt.figure(figsize=(8,5), dpi=80)
    plt.axes(aspect=1)
    plt.pie(counts, #性别统计结果
            labels=labels, #性别展示标签
            colors=colors, #饼图区域配色
            labeldistance = 1.1, #标签距离圆点距离
            autopct = '%3.1f%%', #饼图区域文本格式
            shadow = False, #饼图是否显示阴影
            startangle = 90, #饼图起始角度
            pctdistance = 0.6 #饼图区域文本距离圆点距离
    )
    plt.legend(loc='upper right',)
    plt.title('%s的微信好友性别组成' % friends[0]['NickName'])
    plt.show()
def analyseLocation(friends):
    headers = ['NickName','Province','City']
    with open('wechat_location.csv','w',encoding='utf-8',newline='',) as csvFile:
        writer = csv.DictWriter(csvFile, headers)
        writer.writeheader()
        for friend in friends[1:]:
           row = {}
           row['NickName'] = friend['NickName']
           row['Province'] = friend['Province']
           row['City'] = friend['City']
           writer.writerow(row)
           print(row)
    #导出好友地理位置分组数据
    csvFile.close()
def User2dict(User):
    User_dict = {}
    User_dict["NickName"] = User["NickName"] if User["NickName"] else "NaN"
    User_dict["City"] = User["City"] if User["City"] else "NaN"
    User_dict["Sex"] = User["Sex"] if User["Sex"] else 0
    User_dict["Signature"] = User["Signature"] if User["Signature"] else "NaN"
    User_dict["Province"] = User["Province"] if User["Province"] else "NaN"
    return User_dict

friends_list = [User2dict(i) for i in friends]
data = pd.DataFrame(friends_list)
data.to_csv('wechat_data.csv', index=True,encoding='utf-8-sig')# add by zyy 2018年2月27日, encoding='GBK'
analyseSex(data)
analyseLocation(data)

#分割符号
