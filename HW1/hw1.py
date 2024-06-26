# -*- coding: utf-8 -*-
"""HW1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sqtozALuWdJ39VkSDUZWeDhUmqyB62OZ
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/gdrive/', force_remount=True)

os.chdir("/content/gdrive/My Drive/112_2_LATIA/HW1/") # 切換目錄
!ls -l "/content/gdrive/My Drive/112_2_LATIA/HW1/" # 列出目錄下的檔案

def question_1(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)

    # 提取主要專業科目
    data = df[["major"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"主科:{row[0]}")

    data_grouped = data.groupby("major")
    major = data_grouped["major"].count()
    # 繪出派圖
    plt.pie(major, labels=major.index)
    plt.axis("equal")
    plt.title("College")
    plt.show()

    save_path = os.path.join(folder, 'Question1.png')
    plt.savefig(save_path)

def question_2(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 建立一個新的欄目cost做tuition、housing、food、transportation與books_supplies的總和
    df['cost'] = df[["tuition", "housing", "food", "transportation", "books_supplies"]].mean(axis=1).fillna(0)
    # 提取主要專業科目、與必要花費
    data = df[["major", "cost"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"主要專業科目:{row[0]}\t必要花費:{row[1]}")

    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    data.boxplot(column="cost", by="major")
    # 添加標籤和標題
    plt.title('Major and Significant cost')
    plt.xlabel('major')
    plt.ylabel('cost')

    save_path = os.path.join(folder, 'Question2.png')
    plt.savefig(save_path)

def question_3(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取月收入、學費
    data = df[["monthly_income", "tuition"]]

    # 印出資料
    for index, row in data.iterrows():
        print(f"月收入:{row[0]}\t學費:{round(row[1])}")

    ## 建立圖表
    plt.figure()
    # 繪製散點圖
    plt.scatter(data["monthly_income"], data["tuition"])
    # 添加標籤和標題
    plt.title('Student\'s tuitions and income')
    plt.xlabel('monthly_income')
    plt.ylabel('tuition')

    save_path = os.path.join(folder, 'Question3.png')
    plt.savefig(save_path)


def question_4(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 建立一個新的欄目cost做tuition、housing、food、transportation與books_supplies的總和
    df['cost'] = df[["tuition", "housing", "food", "transportation", "books_supplies"]].mean(axis=1).fillna(0)
    # 提取受到經濟援助、必要花費
    data = df[["financial_aid", "cost"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"受到經濟援助:{row[0]}\t必要花費:{round(row[1])}")

    ## 建立圖表
    plt.figure()
    # 繪製散點圖
    plt.scatter(data["financial_aid"], data["cost"])
    # 添加標籤和標題
    plt.title('Student\'s financial_aid and cost')
    plt.xlabel('financial_aid')
    plt.ylabel('cost')

    save_path = os.path.join(folder, 'Question4.png')
    plt.savefig(save_path)

def question_5(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取性別、與健康與保健消費
    data = df[["gender", "health_wellness"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"性別:{row[0]}\t健康與保健消費:{row[1]}")

    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    data.boxplot(column="health_wellness", by="gender")
    # 添加標籤和標題
    plt.title('Gender and Health_wellness')
    plt.xlabel('gender')
    plt.ylabel('health_wellness')

    save_path = os.path.join(folder, 'Question5.png')
    plt.savefig(save_path)


def question_6(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取主要專業科目、與受到經濟援助
    data = df[["major", "financial_aid"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"主要專業科目:{row[0]}\t受到經濟援助:{row[1]}")

    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    data.boxplot(column="financial_aid", by="major")
    # 添加標籤和標題
    plt.title('Major and financial_aid')
    plt.xlabel('major')
    plt.ylabel('financial_aid')

    save_path = os.path.join(folder, 'Question6.png')
    plt.savefig(save_path)


if __name__ == '__main__':
    csv_file = 'student_spending.csv'

    folder_name = f'Pics of analysis'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    print("學習不同主科的人數：")
    question_1(csv_file, folder_name)

    print("學習不同主科的人與總花費之間之關係：")
    question_2(csv_file, folder_name)

    print("月收入與必要相關花費之關係(包含學費、住宿、食品、交通、書籍)：")
    question_3(csv_file, folder_name)

    print("受到經濟援助與必要相關花費之關係(包含學費、住宿、食品、交通、書籍)：")
    question_4(csv_file, folder_name)

    print("學生性別與健康與保健相關花費之關係：")
    question_5(csv_file, folder_name)

    print("學生專業領域與受到經濟援助之關係：")
    question_6(csv_file, folder_name)