import itchat
import pandas as pd
from pyecharts import Geo, Bar



itchat.login()
friends = itchat.get_friends(update=True)[0:]

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

#分割符号
