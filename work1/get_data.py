# encoding=gbk
import requests
import pandas as pd
import time
import re
from tqdm import trange

topic = "�����"
epochs = 100

def get_data():
    # # csv�ļ�������
    # title1 = [("id", "comment")]  # �б�
    # title2 = pd.DataFrame(title1)  # DataFrame��ʽ
    # title2.to_csv('%s_plus.csv' % topic, header=False, index=False, mode='a+')
    # # mode='a+'ָ���ļ���"׷��"ģʽ�򿪣�����ļ��Ѵ��ڣ���DataFrame��ӵ��ļ�ĩβ������ļ������ڣ��򴴽�һ�����ļ�

    data2 = pd.DataFrame([("id", "comment")])
    data2.to_csv('%s.csv' % topic, header=False, index=False)  # �������ݵ�{topic}.csv

    # ��ȡ��ҳheader��cookie
    header = {'Content-Type': 'application/json; charset=utf-8',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                            'Chrome/76.0.3809.100 Safari/537.36'}
    Cookie = {
        'Cookie': 'SUHB=0nl-t-jpott3lQ; '
                  'SCF=ArfHZrR50j2dIBHthBCgbug0SIY3DMTR8lWwBE7L5h_ANIIE_nFkxL5wEMvyK4SIdpZcQIvW3HE8r_9YaG1GqSs.; '
                  'ALF=1590484838; _T_WM=75965031443; XSRF-TOKEN=521d8f; WEIBOCN_FROM=1110006030; '
                  'SSOLoginState=1587892841; SUB=_2A25zoSI5DeRhGeBG41sW8SzNwjWIHXVRak5xrDV6PUJbktANLVfFkW1NQfza9ocru9'
                  '-jgkjuLFGSId3vfab05o_d; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFI3IIVqQEH4F-YPcpzGZQr5JpX5K-hUgL'
                  '.FoqR1h.NeKzp1K.2dJLoIpQLxK-L1K2LBo-LxK-L1K2LBo-peKzEeLY0e7tt; MLOGIN=1; '
                  'M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E7%25BD%2597%25E5%25BF%2597'
                  '%25E7%25A5%25A5%26uicode%3D10000011%26fid%3D231522type%253D1%2526t%253D10%2526q%253D%2523%25E7%25BD'
                  '%2597%25E5%25BF%2597%25E7%25A5%25A5%25E9%2581%2593%25E6%25AD%2589%2523'}
    print("��ʼ��ȡ����")
    # ��ȡ����
    for ii in trange(epochs):
        url_base = \
            'https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D60%26q%3D%23{}%23%26t%3D10&extparam=%23{' \
            '}%23&luicode=10000011&lfid=102803&page_type=search   all&page= '.format(topic, topic)
        url = url_base + str(ii + 1)

        json = requests.get(url, headers=header, cookies=Cookie)
        try:
            if len(json['data']['cards']) == 0:
                print("��ȡ����")
                return
            for jj in range(len(json['data']['cards'])):
                # print(json['data']['cards'][jj]['mblog']['isLongText'])

                text = re.sub(r'<.*?>', '', json['data']['cards'][jj]['mblog']['text'])  # ȥӢ�����ֺͲ��ַ���
                data1 = [(json['data']['cards'][jj]['mblog']['user']['screen_name'], text)]

                data2 = pd.DataFrame(data1)
                data2.to_csv('%s.csv' % topic, header=False, index=False, mode='a+')  # �������ݵ�{topic}.csv
        except:
            print("��%dҳץȡʧ��" % ii)
        time.sleep(3)
        # ��ֹ��Ƶ������ȡ����ֹ


if __name__ == "__main__":
    get_data()
