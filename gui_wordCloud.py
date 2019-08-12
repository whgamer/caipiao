import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread
import jieba
#.txt
with open('sd-stu1.txt','rt', encoding='UTF-8') as f:
    data =f.read()
str_speech = str(data)
jieba.load_userdict('userdict.txt') #加载本地字典
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))
# str_test ="小明硕士毕业于中国科学院计算所，后在日本京都大学深造"
# seg_list = jieba.cut_for_search(str_test)  # 搜索引擎模式
print(", ".join(seg_list))
seg_list = jieba.cut(str_speech, cut_all=False)  # 默认是精确模式

# print(",".join(seg_list))
list_speech_tem =str((",".join(seg_list)))#添加分隔符

#添加词云图
list_speech_cy =list((" ".join(seg_list)))#添加分隔符
# print('词云图：'+list_speech_cy)

#读入背景图片

bg_pic = imread('motuoche.jpg')

#生成词云

my_wordcloud = WordCloud(mask=bg_pic,background_color='white',scale=1.5).generate(str(list_speech_tem))

image_colors = ImageColorGenerator(bg_pic)
# my_wordcloud = WordCloud().generate(str(list_speech_tem))

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

list_speech = [str(x) for x in list_speech_tem.split(',')]#按照分隔符分割
list4 = list(filter(lambda x : is_needed(x), list_speech))# 去除掉标点符号和不需要的助词
list_speech = list4
from collections import     Counter
word_counts =Counter(list_speech)
top_ten =word_counts.most_common(50)
print(top_ten)