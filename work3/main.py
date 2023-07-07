# -*- coding: utf-8 -*-
# @Author  : zqbai
# @Time    : 2023/4/1 下午5:09
# @Function: 

import pandas
import matplotlib.pyplot as plt

data = pandas.DataFrame({
        'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'height': [149, 153, 156, 156, 161, 162, 162, 162, 164, 165],
        'weight': [45, 49, 46, 49, 54, 52, 57, 49, 51, 52]

    })

if __name__ == '__main__':
    print("身高均值：", data['height'].mean())
    print("身高标准差：", data['height'].std())
    print("身高中位数：", data['height'].median())
    print("第一个四分位数：", data['height'].quantile(0.25))
    print("第三个四分位数：", data['height'].quantile(0.75))

    # 设置画布大小和字体大小
    plt.rcParams['figure.figsize'] = [8, 6]
    plt.rcParams['font.size'] = 12

    # 绘制身高和体重的盒须图
    data.boxplot(column=['height', 'weight'])
    plt.title('Boxplot of Height and Weight')
    plt.ylabel('Values')
    plt.savefig('盒须图.png')
    plt.show()

    # 绘制身高和体重的散点图
    plt.scatter(data['height'], data['weight'])
    plt.title('Scatter Plot of Height and Weight')
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.savefig('散点图.png')
    plt.show()