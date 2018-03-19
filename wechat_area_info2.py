import pandas as pd
from pyecharts import Geo, Bar
def Cal_mVw(data):
    result = {}
    for i in data:
        if i == 1:
            result["man"] = result.get("man", 0) + 1
        elif i == 2:
            result["woman"] = result.get("woman", 0) + 1
        else:
            result["unknown"] = result.get("nunknown", 0) + 1
    return result


def count_city(data):
    result = {}
    for i in data:
        if data is not "NaN" or data is not "nan":
            result[i] = result.get(i, 0) + 1
    return result

data1 = pd.read_csv('wechat_data.csv',encoding='utf-8-sig')#, encoding='GBK'
manVSwoman=Cal_mVw(data1["Sex"])
#print(manVSwoman)
bar = Bar("个人微信好友男女比例")
bar.add("男女人数", ["男", "女", "不详"], [139, 75, 1])
bar.render()

city=count_city(data1["City"])
geo = Geo("微信好友分布", "", title_color="#fff", title_pos="center",
width=1200, height=600, background_color='#404a59')
# attr, value = geo.cast(city)
geo.add("", city.keys(), city.values(), visual_range=[0, 30], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
geo.show_config()
geo.render()