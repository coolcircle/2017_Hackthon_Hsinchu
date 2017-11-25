# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 05:39:59 2017

@author: USER
"""

import pandas as pd 
import os
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import csv
import numpy as np
from scipy import stats, integrate
from numpy import nan
import requests
from xml.etree import ElementTree
import folium
import chardet

path = 'C:/Users/USER/Desktop/hackson/資料'
os.chdir(path)

#資料讀取
with open('BinesLocaWi.csv', 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large

data = pd.read_csv('BinesLocaWi.csv', encoding=result['encoding'])


#資料讀取2
with open('hotspot_stat2.csv', 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large

data = pd.read_csv('hotspot_stat2.csv', encoding=result['encoding'])




#敘述統計
#將類別變數用數值替換
#-1.熱點類別
set(data['熱點類別'])
data['熱點類別'][data['熱點類別']=='旅遊景點'] = 1
data['熱點類別'][data['熱點類別']=='大眾運輸節點'] = 2
data['熱點類別'][data['熱點類別']=='文教館所'] = 3
data['熱點類別'][data['熱點類別']=='洽公場所'] = 4
data['熱點類別'][data['熱點類別']=='公車熱點'] = 5
data['熱點類別'][data['熱點類別']=='功能性場館'] = 5

#-2.鄉鎮市區
set(data['鄉鎮市區'])
data['鄉鎮市區'][pd.isnull(data['鄉鎮市區'])] = 0
data['鄉鎮市區'][data['鄉鎮市區']=='香山區'] = 1
data['鄉鎮市區'][data['鄉鎮市區']=='北區'] = 2
data['鄉鎮市區'][data['鄉鎮市區']=='東區'] = 3

"""
#-1.畫分布圖
import seaborn as sns
x = data4['使用人']
a = x
hist, bins = np.histogram(a, bins=100, normed=True)
bin_centers = (bins[1:]+bins[:-1])*0.5
plt.plot(bin_centers, hist)
"""
#summary
summary = pd.DataFrame(data.describe())

#-2畫box plot
# basic plot
#data4.columns
for i in data.columns[3:]:
    print(i)
    x = data[i]
    plt.figure()
    plt.boxplot(x)
    fileName = 'boxplot-' + i
    plt.savefig('C:/Users/USER/Desktop/hackson/result/' + fileName + '.png' , dpi=300)


#不分群看連續變數間相關性
#-correlation matrix
correlation = data.corr()
#-畫heatmap


#不分群看類別變數間相關性
#-chi-square test
import scipy.stats as scs


def categories(series):
    return range(int(series.min()), int(series.max()) + 1)


def chi_square_of_df_cols(df, col1, col2):
    df_col1, df_col2 = df[col1], df[col2]

    result = [[sum((df_col1 == cat1) & (df_col2 == cat2))
               for cat2 in categories(df_col2)]
              for cat1 in categories(df_col1)]

    return scs.chi2_contingency(result)



print(chi_square_of_df_cols(data, '熱點類別', '鄉鎮市區'))
#--'熱點類別', '鄉鎮市區'→相關→表示某些區域的熱點傾向於某種類別


#分5群看連續變數間相關性
#data.columns
Attr = data.columns[3:8]
for attr in Attr:
    try:
        #-依據attr排序
        Sdata = pd.DataFrame(data.sort_values(by=[attr], ascending=False)).reset_index(drop = True)
        #-畫排名直方圖
        def PlotBar(yterm,title): 
            plt.figure(figsize=(38,15))
            y = Sdata[yterm][0:30]
            x = range(len(y))
            xticks1 = Sdata['熱點名稱'][0:30]
            plt.xticks(x,xticks1,size=38,rotation=270)
            plt.yticks(size = 38)
            width = 0.8
            plt.bar(x, y, width, color="blue")
            plt.suptitle(title, size = 55)
            
        NN = '106/10新竹免費Wifi─' + attr +'統計圖'
        PlotBar(attr,NN)
        plt.savefig('C:/Users/USER/Desktop/hackson/result/' + attr + '排序.png' , dpi=300)
        
        
        
        #-分5群，
        C = 5
        cluster = np.array_split(Sdata, C)
        """
        #分群資料存檔
        os.chdir('C:/Users/USER/Desktop/hackson/heatmapData')
        for i in range(C):
            NN = 'cluster' + str(i) + '.csv'
            cluster[i].to_csv(NN, index=False)
        """
        #-5群的相關係數矩陣存在字典corrC中
        corrC2 = {}
        corrC = {}
        for i in range(len(cluster)):
            temp = cluster[i].corr()
            NN = 'cluster' + str(i)
            corrC[NN] = temp
            
        corrC2[attr] = corrC
        
        
        #-畫heatmap
        
        
        #分5群看類別變數間相關性
        corrCCa2 = {}
        corrCCa = {}
        for i in range(len(cluster)):
            temp = chi_square_of_df_cols(cluster[i], '熱點類別', '鄉鎮市區')
            NN = 'cluster' + str(i)
            corrCCa[NN] = temp
        
        corrCCa2[attr] = corrCCa
    except:
        print(attr)
    
    
#依類別分類看連續變數間相關性
len(set(data['熱點類別']))

wifitype = list(set(data['熱點類別']))

for q in wifitype:
    temp = data[data['熱點類別'] == q]
    os.chdir('C:/Users/USER/Desktop/hackson/heatmapData2')
    NN = 'cluster-' + q + '.csv'
    temp.to_csv(NN, index=False)