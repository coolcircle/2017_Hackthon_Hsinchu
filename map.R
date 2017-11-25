## 
library(rworldmap)
newmap <- get_map(location = 'Hsinchu', zoom = 13)
ggmap(map)

##
setwd("C:/Users/Joshua/Desktop/蔬菜價格/wifi_data")
x = read.csv("BinesLocaWi.csv",sep=",",header = T);head(x)
colnames(x) = c(1,2,3,4,5,6,7,8,9,10,11,12,"lon","lat")

cbind(na.omit(x[,13:14]),2)
gdata = cbind(na.omit(x[,13:14]),2);colnames(gdata)=c("lon","lat","si")
ggmap(map) + geom_point(aes(x = lon, y = lat, size = ), data = gdata, alpha = 0.5,col=2)

geom_point(aes(x=24.81,y=120.97, data = x, alpha = .5))
?geom_point
points(x$lon, x$lat , col = "red", cex = 10)


?geom_point

x$lon
x$lat
class(x[,13:14])






















library(ggmap)
airports <- read.csv("http://openflights.svn.sourceforge.net/viewvc/openflights/openflights/data/airports.dat", header = FALSE)
colnames(airports) <- c("ID", "name", "city", "country", "IATA_FAA", "ICAO", "lat", "lon", "altitude", "timezone", "DST")
head(airports)

routes <- read.csv("http://openflights.svn.sourceforge.net/viewvc/openflights/openflights/data/routes.dat", header=F)
routes = read.csv("airlines.txt")
dim(routes)
colnames(routes) <- c("airline", "airlineID", "sourceAirport", "sourceAirportID", "destinationAirport", "destinationAirportID", "codeshare", "stops")
head(routes)

library(plyr)
departures <- ddply(routes, .(sourceAirportID), "nrow")
names(departures)[2] <- "flights"
arrivals <- ddply(routes, .(destinationAirportID), "nrow")
names(arrivals)[2] <- "flights"

airportD <- merge(airports, departures, by.x = "ID", by.y = "sourceAirportID")






