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
        # ���ð�PIL�е�open��������ȡͼƬ�ļ���ͨ��numpy�е�array������������
        wordcloud = WordCloud(width=3000,
                              height=3000,
                              font_path="font.ttf",  # �����ļ�
                              background_color="white",  # ���ñ�����ɫ
                              max_font_size=150,  # �����������ֵ
                              max_words=2000,  # ���������ʾ������
                              stopwords=stop_words,
                              # ����ͣ�ôʣ�ͣ�ô����ٴ���ͼ�б�ʾ
                              ).generate(text)
        image = wordcloud.to_image()
        wordcloud.to_file(topic.split('.')[0] + '-ciyun.png')  # �����ļ�
        image.show()


if __name__ == "__main__":
    ciyun()
