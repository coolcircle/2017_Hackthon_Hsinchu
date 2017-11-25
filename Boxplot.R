## correlation heatmap
setwd("C:/Users/Joshua/Desktop/蔬菜價格/wifi_data")
library(ggplot2)
library(data.table)
x = read.csv("hotspot_stat2.csv",sep=",",header = T);
head(x)

# 使用人次
png("使用人次.png",width = 580, height = 480)
p = ggplot(x, aes(x=`熱點類別`, y=`使用人次`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("使用人次") + xlab("") +
   theme(plot.title = element_text(color="black",size=14,face = "bold"),
          axis.text.x = element_text(size = 8))

# 使用人數
p = ggplot(x, aes(x=`熱點類別`, y=`使用人數`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("使用人數") + xlab("")
  + theme(plot.title = element_text(color="black",size=14,face = "bold"))

# 總分鐘數
p = ggplot(x, aes(x=`熱點類別`, y=`總分鐘數`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("總分鐘數") + xlab("")
+ theme(plot.title = element_text(color="black",size=14,face = "bold"))

# 每人使用分鐘數
p = ggplot(x, aes(x=`熱點類別`, y=`每人使用分鐘數`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("每人使用分鐘數") + xlab("") + 
    theme(plot.title = element_text(color="black",size=14,face = "bold"))

# 總流量.MB
p = ggplot(x, aes(x=`熱點類別`, y=`總流量.MB`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("總流量.MB") + xlab("")
+ theme(plot.title = element_text(color="black",size=14,face = "bold"))

# 平均每人使用流量
p = ggplot(x, aes(x=`熱點類別`, y=`平均每人使用流量`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("平均每人使用流量") + xlab("")
+ theme(plot.title = element_text(color="black",size=14,face = "bold"))

# 平均每分鐘使用流量
p = ggplot(x, aes(x=`熱點類別`, y=`平均每分鐘使用流量`)) + geom_boxplot(aes(group=`熱點類別`)) 
p + ylab("平均每分鐘使用流量") + xlab("")
+ theme(plot.title = element_text(color="black",size=14,face = "bold"))





