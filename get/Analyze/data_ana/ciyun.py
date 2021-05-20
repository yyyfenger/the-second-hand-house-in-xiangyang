from wordcloud import WordCloud
import jieba
from imageio import imread

filename = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\ershoufang-clean-mini-utf8.csv"
backpicture = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\house1.jpg"
savepicture = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\襄阳二手房词云.png"
fontpath = "C:\\Users\\bingo\\Desktop\\毕设\\test\\get\\Analyze\\file\\simhei.ttf"
stopwords = ["null", "暂无", "数据", "照片", "房本"]
comment_text = open(filename, encoding="utf-8").read()
color_mask = imread(backpicture)
ershoufang_words = jieba.cut(comment_text)
ershoufang_words = [word for word in ershoufang_words if word not in stopwords]
cut_text = " ".join(ershoufang_words)

cloud = WordCloud(

    font_path=fontpath,
    background_color='white',
    mask=color_mask,
    max_words=2000,
    max_font_size=60

)
word_cloud = cloud.generate(cut_text)
word_cloud.to_file(savepicture)
