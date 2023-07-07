# encoding=gbk
import pandas as pd
import jieba
from wordcloud import WordCloud
from stopwords import stop_words
import os


def chinese_jieba(text):
    wordlist_jieba = jieba.cut(text)
    space_wordlist = " ".join(wordlist_jieba)
    return space_wordlist


def ciyun():
    topic_list = [f for f in os.listdir('../work1/') if f.endswith('.csv')]
    for topic in topic_list:
        df = pd.read_csv('../work1/' + topic)
        comment_list = df['comment'].values.tolist()
        text = ""
        for jj in range(len(comment_list)):
            text = text + chinese_jieba(comment_list[jj])
        print(text)
        # 调用包PIL中的open方法，读取图片文件，通过numpy中的array方法生成数组
        wordcloud = WordCloud(width=3000,
                              height=3000,
                              font_path="font.ttf",  # 字体文件
                              background_color="white",  # 设置背景颜色
                              max_font_size=150,  # 设置字体最大值
                              max_words=2000,  # 设置最大显示的字数
                              stopwords=stop_words,
                              # 设置停用词，停用词则不再词云图中表示
                              ).generate(text)
        image = wordcloud.to_image()
        wordcloud.to_file(topic.split('.')[0] + '-ciyun.png')  # 导出文件
        image.show()


if __name__ == "__main__":
    ciyun()
