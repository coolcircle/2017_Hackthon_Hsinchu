setwd('C:/Users/USER/Desktop/hackson/data')
getwd()


Data = read.csv("wifi.csv",sep=",",header=T)
head(Data)

data = read.csv("BinesLocaWi.csv",sep=",",header=T)
#data = read.csv("NAout.csv",sep=",",header=T)
head(data)

summary(data)

data.columns

#將類型改為
#1:旅遊景點
#2.大眾運輸節點
#3.洽公場所
#4.文教館所
#5.其他

data$熱點類別 <- gsub('旅遊景點', '1', data$熱點類別)
data$熱點類別 <- gsub('大眾運輸節點', '2', data$熱點類別)
data$熱點類別 <- gsub('洽公場所', '3', data$熱點類別)
data$熱點類別 <- gsub('文教館所', '4', data$熱點類別)
data$熱點類別 <- gsub('其他', '5', data$熱點類別)
data$熱點類別[is.na(data$熱點類別)] <- 0

View(data)

#將鄉鎮市區改為
#1:東區
#2.北區
#3.香山區

data$鄉鎮市區 <- gsub('東區', '1', data$鄉鎮市區)
data$鄉鎮市區 <- gsub('北區', '2', data$鄉鎮市區)
data$鄉鎮市區 <- gsub('香山區', '3', data$鄉鎮市區)
data$鄉鎮市區[is.na(data$鄉鎮市區)] <- 0

View(data)

####畫關係圖(依使用人次)
data2 <- data[order(data$使用人次, decreasing = TRUE),]
#28個一組(每28個取平均)
c1 = data2[1:28,4:11]

zaa <- colMeans(c1[,1:6], na.rm = TRUE)
zab <- colMeans(as.numeric(as.character(c1[,7])), na.rm = TRUE)

typeof(c1[,8])

c2 = data2[29:56,4:11]
c3 = data2[57:84,4:11]
c4 = data2[85:112,4:11]
c5 = data2[113:nrow(data2),4:11]

data2[1,1]
row.names(data2) <- data$熱點名稱
data_matrix = data2[,5:11]
data_matrix <- data.matrix(data_matrix)
data_heatmap <- heatmap(data_matrix, Rowv=NA, Colv=NA, col = brewer.pal(9, "Blues"), scale="column", margins=c(5,10))








library(plotly)
m <- matrix(rnorm(9), nrow = 3, ncol = 3)
p <- plot_ly(
  x = c("a", "b", "c"), y = c("d", "e", "f"),
  z = m, type = "heatmap"
)

# Create a shareable link to your chart
# Set up API credentials: https://plot.ly/r/getting-started
chart_link = plotly_POST(p, filename="heatmap/cat")
chart_link

























############################################
x = read.csv("RicePrice.csv",sep=",",fileEncoding = "UTF8");head(x)

x = read.csv("NAout.csv",sep=',',header=T)
a = read.csv("productSituation.csv",sep=',',header=T)
#
a<- read.table("RicePrice.csv", header = T, sep = ",", encoding = 'utf-8')

data <- read.csv("RicePrice.csv") 
a<- read.csv("RicePrice.csv", header = TRUE, sep = ",")

#糧價
RicePrice = pd.read_csv('RicePrice.csv')

#臺灣地區蔬菜生產概況
Situation = pd.read_csv('productSituation.csv')
