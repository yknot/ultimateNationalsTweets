library(ggplot2)

nattys <- read.csv("data/nattys.csv")
ultilive <- read.csv("data/ultilive.csv")


nattys.date.trim <- nattys[as.Date(nattys$Posted.at) >= "2014-10-16" & as.Date(nattys$Posted.at) <= "2014-10-19",]     
ultilive.date.trim <- ultilive[as.Date(ultilive$Posted.at) >= "2014-10-16" & as.Date(ultilive$Posted.at) <= "2014-10-19",]     

# combine into one dataframe
tweets <- rbind.data.frame(nattys.date.trim, ultilive.date.trim)

tweets$ultiworld[tweets$Screen.name == "Ultiworldlive"] <- "UltiworldLive"
tweets$ultiworld[tweets$Screen.name != "Ultiworldlive"] <- "#NationalsTX"

tweets$Posted.at <- as.POSIXct(tweets$Posted.at)


# nationals tweets
hist(nattys.date.trim$Posted.at, breaks = 'h', freq = TRUE, format = "%H", main= "#nationalsTX Tweets per Hour", xlab= "Hours of Oct 16 - 19")


# Ultiworld tweets
hist(as.POSIXct(ultilive.date.trim$Posted.at), breaks = 'h', freq = TRUE, format = "%H", main= "Ultiworld_Live Tweets per Hour", xlab= "Hours of Oct 16 - 19")



ggplot(tweets[tweets$Screen.name != "Ultiworldlive",],
       aes(x=as.POSIXct(Posted.at), group=ultiworld, fill=as.factor(ultiworld))) +
      geom_histogram(position="dodge", breaks = "h", right = TRUE) + 
      scale_fill_discrete(name="Day") +
      theme_bw(base_size=20) +
      xlab ("values") +
      scale_x_continuous(breaks = as.POSIXct(tweets$Posted.at))
