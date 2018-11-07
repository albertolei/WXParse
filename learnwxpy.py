from wxpy import *
from snownlp import SnowNLP, sentiment
import re, jieba
from scipy.misc import imread
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import matplotlib.pyplot as plt
from collections import Counter
import pandas as pd

bot = Bot()
friends = bot.friends()
groups=bot.groups()
mps = bot.mps()
#sex
# sex_dict = {
#     'boy':0,
#     'girl':0,
#     'other':0
# }
# for friend in friends:
#     if friend.sex == 1:
#         sex_dict['boy'] += 1
#     elif friend.sex == 2:
#         sex_dict['girl'] += 1
#     else:
#         sex_dict['other'] += 1
# labels = ['boy', 'girl', 'other']
# colors = ['red', 'yellow', 'green']
# explode = (0.1, 0, 0)
# plt.figure(figsize=(8,5), dpi=80)
# plt.axes(aspect=1)
# plt.pie(sex_dict.values(), explode=explode, labels=labels, autopct='%1.2f%%',colors=colors, labeldistance=1.1, shadow=True, startangle=90, pctdistance=0.6)
# plt.title('SEX ANALYSIS', bbox = dict(facecolor='g', edgecolor='blue', alpha=0.65))
# plt.savefig('sex_analysis.jpg')
# plt.show()

# place
# city = []
# Municipality = ['上海', '上海市', '北京', '北京市', '重庆', '重庆市', '天津', '天津市']
# for friend in friends:
#     if friend.province in Municipality:
#         city.append(friend.province)  #直辖市相当省
#     else:
#         city.append(friend.city)

# counts = dict(Counter(city))
# print(counts)
# df = pd.DataFrame([counts]).T
# df.to_excel('city.xlsx')

# emotion
text1 = []
emotions = []
for friend in friends:
    sig = friend.signature.strip()
    newsig = re.sub(re.compile('<.*?>|[0-9]|。|，|！|～|—|”|“|《|》|\？|、|：'), '', sig)
    text1.append(newsig)
    if len(newsig) > 0:
        sentiments = SnowNLP(newsig).sentiments
        emotions.append(sentiments)

text = "".join(text1)
wordlist = "".join(jieba.cut(text, cut_all=True))
stopwords = STOPWORDS
bgimg = imread(r'd:/brige.jpg')
# font_path=r'C:/Windows/Fonts/Consolas.ttf'
wc = WordCloud( 
               background_color = 'white',
               max_words=2000,
               stopwords = stopwords,
               mask=bgimg,
               max_font_size=100,
               random_state=42,
               width=1000,
               height=860,
               margin=2).generate(wordlist)
image_colors = ImageColorGenerator(bgimg)
plt.imshow(wc)
plt.axis('off')
plt.savefig('sig.jpg')
plt.show()


  