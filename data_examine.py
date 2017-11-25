# -*- coding: utf-8 -*-
import os
import pandas as pd

path = 'C:/Users/USER/Desktop/hackson/資料'
os.chdir(path)


#糧價
RicePrice = pd.read_csv('RicePrice.csv')

#臺灣地區蔬菜生產概況
Situation = pd.read_csv('productSituation.csv')

len(set(Situation['蔬菜類別']))

Data2013 = Situation[Situation['年度']==2013][:]
Data2014 = Situation[Situation['年度']==2014][:]
Data2015 = Situation[Situation['年度']==2015][:]
Data2016 = Situation[Situation['年度']==2016][:]

