## correlation heatmap
setwd("C:/Users/Joshua/Desktop/蔬菜價格/wifi_data")
library(ggplot2)
library(data.table)
plotCor = function(corMat){
  upper_tri <- get_upper_tri(corMat)
  # Melt the correlation matrix
  melted_cormat <- melt(upper_tri, na.rm = TRUE)
  # Create a ggheatmap
  ggheatmap <- ggplot(melted_cormat, aes(Var2, Var1, fill = value))+
    geom_tile(color = "white")+
    scale_fill_gradient2(low = "blue", high = "red", mid = "white", 
                         midpoint = 0, limit = c(-1,1), space = "Lab", 
                         name="Pearson\nCorrelation") +
    theme_minimal()+ # minimal theme
    theme(axis.text.x = element_text(angle = 45, vjust = 1, 
                                     size = 12, hjust = 1),
          axis.text.y = element_text(angle = 0, vjust = 1, 
                                     size = 12, hjust = 1))+
    coord_fixed()
  # Print the heatmap
  # print(ggheatmap)
  
  ggheatmap + 
    geom_text(aes(Var2, Var1, label = value), color = "black", size = 4) +
    theme(
      axis.title.x = element_blank(),
      axis.title.y = element_blank(),
      panel.grid.major = element_blank(),
      panel.border = element_blank(),
      panel.background = element_blank(),
      axis.ticks = element_blank(),
      legend.justification = c(1, 0),
      legend.position = c(0.4, 0.7),
      legend.direction = "horizontal")+
    guides(fill = guide_colorbar(barwidth = 7, barheight = 1,
                                 title.position = "top", title.hjust = 0.5))
}
get_upper_tri <- function(cormat){
  cormat[lower.tri(cormat)]<- NA
  return(cormat)
}

##
x = read.csv("cluster0.csv",sep=",",header = T)
x = read.csv("cluster1.csv",sep=",",header = T)
x = read.csv("cluster2.csv",sep=",",header = T)
x = read.csv("cluster3.csv",sep=",",header = T)
x = read.csv("cluster4.csv",sep=",",header = T)
x = read.csv("BlinesLocalWi.csv",sep=",",header = T)

xx = x[,4:9];
plotCor(round(cor(xx),3))
# cor(xx)

png("cluster0.png",width = 580, height = 480)
png("cluster1.png",width = 580, height = 480)
png("cluster2.png",width = 580, height = 480)
png("cluster3.png",width = 580, height = 480)
png("cluster4.png",width = 580, height = 480)
png("wifi_all.png",width = 580, height = 480)

dev.off()

