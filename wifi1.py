# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:22:21 2017

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


path = 'C:/Users/USER/Desktop/hackson/資料'
os.chdir(path)

#讀資料
data1 = pd.read_csv("wifi.csv", encoding = 'utf8')
data2 = pd.read_csv("WifiLocation.csv", encoding = 'utf8')
data3 = pd.read_csv("locate.csv", encoding = 'utf8')
data4 = pd.read_csv("BinesLocaWi.csv", encoding='encoding')



import chardet

with open('BinesLocaWi.csv', 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large


data4 = pd.read_csv('BinesLocaWi.csv', encoding=result['encoding'])

data4.columns = ['經度','緯度']

#data2.to_csv('NN.csv', index=False)

#使用人次/使用人數/使用分鐘數排名
sort11 = pd.DataFrame(data1.sort_values(by=['使用人次'], ascending=False))


#畫排名直方圖
def PlotBar(yterm,title):
    sort11 = pd.DataFrame(data1.sort_values(by=[yterm], ascending=False))
    
    plt.figure(figsize=(38,15))
    y = sort11[yterm][0:30]
    x = range(len(y))
    xticks1 = sort11['熱點名稱'][0:30]
    plt.xticks(x,xticks1,size=38,rotation=270)
    plt.yticks(size = 38)
    width = 0.8
    plt.bar(x, y, width, color="blue")
    plt.suptitle(title, size = 55)
        

#-畫圖
PlotBar('使用人次','106/10新竹免費Wifi─使用人次統計圖')
PlotBar('使用人數','106/10新竹免費Wifi─使用人數統計圖')
PlotBar('總分鐘數','106/10新竹免費Wifi─總分鐘數統計圖')
PlotBar('總流量-MB','106/10新竹免費Wifi─總流量統計圖')



#表格彙整
term = '總流量-MB'
sort11 = pd.DataFrame(data1.sort_values(by=[term], ascending=False)).reset_index(drop = True)
result = pd.concat([sort11['熱點名稱'], sort11[term]], axis = 1)

#-存檔
path = 'C:/Users/USER/Desktop/hackson/result'
os.chdir(path)
NN = 'wifi排序-' + term + '.csv'
result.to_csv(NN, index=False)




#經緯度對照、資料合併
mapresult = []
for i in data1['熱點名稱']:
    try:
        index = list(data2['熱點名稱']).index(i)
        a = [ data3['經度'][index], data3['緯度'][index]]
        mapresult.append(a)
    except:
        mapresult.append(['NA','NA'])
mapresult = pd.DataFrame(mapresult, columns = ['經度','緯度'])



othresult = []
for i in data1['熱點名稱']:
    try:
        index = list(data2['熱點名稱']).index(i)
        a = [data2['熱點類別'][index], data2['鄉鎮市區'][index], data2['地址'][index]]
        othresult.append(a)
    except:
        othresult.append(['NA','NA','NA'])

othresult = pd.DataFrame(othresult, columns = ['熱點類別','鄉鎮市區','地址'])
  
        

Data = pd.concat([data1, othresult, mapresult], axis = 1)
Data.to_csv('BinesLocaWi.csv', index=False)    


#刪除Data中有遺失值的row→剩下96個地點(原本139)
ddd = Data[Data.熱點類別 != 'NA'].reset_index(drop = True)
ddd.to_csv('NAout.csv', index=False)


#敘述統計
#-將類別變數用數值替換
#-1.熱點類別
set(data4['熱點類別'])
data4['熱點類別'][data4['熱點類別']=='旅遊景點'] = 1
data4['熱點類別'][data4['熱點類別']=='大眾運輸節點'] = 2
data4['熱點類別'][data4['熱點類別']=='文教館所'] = 3
data4['熱點類別'][data4['熱點類別']=='洽公場所'] = 4
data4['熱點類別'][data4['熱點類別']=='其他'] = 5

#-2.鄉鎮市區
set(data4['鄉鎮市區'])
data4['鄉鎮市區'][pd.isnull(data4['鄉鎮市區'])] = 0
data4['鄉鎮市區'][data4['鄉鎮市區']=='香山區'] = 1
data4['鄉鎮市區'][data4['鄉鎮市區']=='北區'] = 2
data4['鄉鎮市區'][data4['鄉鎮市區']=='東區'] = 3

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
summary = pd.DataFrame(data4.describe())

#-2畫box plot
# basic plot
#data4.columns
for i in data4.columns[3:]:
    print(i)
    x = data4[i]
    plt.figure()
    plt.boxplot(x)
    fileName = 'boxplot-' + i
    plt.savefig('C:/Users/USER/Desktop/hackson/result/' + fileName + '.png' , dpi=300)



#看變數間相關性
#-
cluster = [5]*28 + [4]*28 + [3]*28 + [2]*28 + [1]*27
cluster = pd.DataFrame(cluster, columns=['cluster'])
len(data4)

#chi-square test
import scipy.stats as scs


def categories(series):
    return range(int(series.min()), int(series.max()) + 1)


def chi_square_of_df_cols(df, col1, col2):
    df_col1, df_col2 = df[col1], df[col2]

    result = [[sum((df_col1 == cat1) & (df_col2 == cat2))
               for cat2 in categories(df_col2)]
              for cat1 in categories(df_col1)]

    return scs.chi2_contingency(result)

data4 = pd.concat([data4, cluster], axis  = 1)


print(chi_square_of_df_cols(data4, 'cluster', '熱點類別'))
#'cluster', '熱點類別'→相關
print(chi_square_of_df_cols(data4, 'cluster', '鄉鎮市區'))
#'cluster', '鄉鎮市區'→相關
print(chi_square_of_df_cols(data4, '熱點類別', '鄉鎮市區'))
#'熱點類別', '鄉鎮市區'→相關




#-用data4畫相關係數矩陣


#wifitype = data4['熱點類別'].replace('旅遊景點','1').replace('大眾運輸節點','2').replace('洽公場所','3').replace('文教館所','4'). replace('其他','5').replace('NA','0')
#wifitype = pd.DataFrame(wifitype)
#df = pd.concat([df, wifitype],axis = 1)

corelation = data4.corr()


#畫在地圖上
#建立pair list of location
#方法一
import folium
locations = data4[['緯度' ,'經度']]
locations = locations[np.isfinite(locations['緯度'])]
locationlist = locations.values.tolist()
myMap = folium.Map(location=[120.969, 24.8052], zoom_start=12)
for point in range(0, len(locationlist)):
    folium.Marker(locationlist[point], popup=data4['熱點名稱'][point]).add_to(myMap)



#方法二
import folium
locations = data4[['緯度' ,'經度']]
locations = locations[np.isfinite(locations['緯度'])]
locationlist = locations.values.tolist()
display = folium.Map(location=[120.969, 24.8052])

for (_, (lat, long)) in locations.iterrows():
    folium.CircleMarker([lat, long],
                    radius=5,
                    color='#3186cc',
                    fill_color='#3186cc',
                   ).add_to(display)




from IPython.display import HTML, display
myMap._build_map()
mapWidth, mapHeight = (400,500) # width and height of the displayed iFrame, in pixels
srcdoc = myMap.HTML.replace('"', '&quot;')
embed = HTML('<iframe srcdoc="{}" '
             'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
             'border: none"></iframe>'.format(srcdoc, width, height))
embed

term = data4.columns[3]
sort11 = pd.DataFrame(data4.sort_values(by=[term], ascending=False)).reset_index(drop = True)
df = pd.DataFrame(sort11, columns= [data4.columns[3], data4.columns[4],
                                   data4.columns[5], data4.columns[6],
                                   data4.columns[7], data4.columns[8]
                                  ])[0:28]
corelation2 = df.corr()



term = data4.columns[3]
sort11 = pd.DataFrame(data4.sort_values(by=[term], ascending=False)).reset_index(drop = True)
df = pd.DataFrame(sort11, columns= [data4.columns[3], data4.columns[4],
                                   data4.columns[5], data4.columns[6],
                                   data4.columns[7], data4.columns[8]
                                  ])[-28:]
corelation3 = df.corr()






x = np.array(ddd['緯度'])
y = np.array(ddd['經度'])

"""
test = []
for i in range(len(x)):
    oo = str(x[i]) + '-' + str(y[i])
    test.append(oo)
    
len(test)
len(set(test))
"""

ddd['緯度'][0]

# Generate data...
#x = np.random.random(90)
#y = np.random.random(90)

type(x)
len(x)
# Plot...
plt.scatter(x, y, c=y, s=10)
plt.gray()

plt.show()

plt.scatter(x, y, c=ddd['使用人次'], colormap='jet', s=10)
ddd.plot.scatter('緯度', '經度', c='使用人次', colormap='jet')

"""
data = Data
#以地圖呈現結果
import folium
display = folium.Map(location=[50, 120])

for (_, (lat, long)) in data[['經度', '緯度']].iterrows():
    folium.CircleMarker([lat, long],
                    radius=5,
                    color='#3186cc',
                    fill_color='#3186cc',
                   ).add_to(display)

display

import gmplot

