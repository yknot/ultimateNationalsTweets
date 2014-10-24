nattys <- read.csv("data/nattys.csv")
ultilive <- read.csv("data/ultilive.csv")


nattys.date.trim <- nattys[as.Date(nattys$Posted.at) >= "2014-10-16" & as.Date(nattys$Posted.at) <= "2014-10-19",]     
ultilive.date.trim <- ultilive[as.Date(ultilive$Posted.at) >= "2014-10-16" & as.Date(ultilive$Posted.at) <= "2014-10-19",]     


