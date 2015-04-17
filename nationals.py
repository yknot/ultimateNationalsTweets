# pandas for data analysis
import pandas as pd
from pandas.tseries.offsets import *
# datetime for dealing with dates
import datetime as dt
# array
import numpy as np
# plots
import matplotlib.pyplot as plt
# pretty plots
import seaborn as sns



def parseData(file):
    # read csv
    temp = pd.read_csv('data/' + file + '.csv', parse_dates=['Posted at'])
    
    # change index to sort by date not twitter id
    temp.set_index('Posted at', inplace = True)

    # timezone change because nattys was in TX
    temp.index = temp.index - DateOffset(hours=5)    

    # cut out twitter id
    temp = temp[['Text', 'Screen name']]

    # add columns for parts of dates
    temp['month'] = temp.index.month
    temp['day'] = temp.index.day
    temp['hour'] = temp.index.hour
    temp['minute'] = temp.index.minute

    # sort by date
    temp = temp.sort_index(ascending=True)

    # slice data for only during nationals
    start = temp.index.searchsorted(dt.datetime(2014, 10, 16))
    end = temp.index.searchsorted(dt.datetime(2014, 10, 20))
    temp = temp.ix[start:end]    

    return temp


def barplotHours(ultilive, nattys):
    # get hours stats
    ultiliveHours = ultilive.groupby('hour')
    nattysHours = nattys.groupby('hour')
    
    
    # dataframe for hours factorplot
    dfHours = pd.DataFrame(index = np.arange(0,48), columns = ['Hour', 'Tweets', 'Source'])
    
    ulti_hours = sorted(ultilive.hour.unique())
    ulti_values = np.array(ultiliveHours.size())
    
    natty_hours = sorted(nattys.hour.unique())
    natty_values = np.array(nattysHours.size())

    for i in xrange(24):
        dfHours.Hour[i] = i
        dfHours.Source[i] = 'Ultiworld Live'
        
        dfHours.Hour[i+24] = i
        dfHours.Source[i+24] = '#NationalsTX'

    
        if i in ulti_hours:
            dfHours.Tweets[i] = ulti_values[ulti_hours.index(i)]
        else:
            dfHours.Tweets[i] = 0

        if i in natty_hours:
            dfHours.Tweets[i+24] = natty_values[natty_hours.index(i)]
        else:
            dfHours.Tweets[i+24] = 0
            


    # sns settings
    sns.set(style='darkgrid', context='poster')
    plt.figure(figsize=(20,15))
    
    s = sns.barplot('Hour', 'Tweets', 'Source', data=dfHours, palette='Paired')
    s.set_title("Tweets by Hour")

    # save output
    s.figure.savefig("ByHour.png")

    print dfHours


def twentyMins(ultilive, nattys):
    # create array for every 20 minutes from 10-16 00:00 to 10-20 00:00
    ulti_twentyMins = np.zeros(288)

    for u in ultilive.iterrows():
        day = (u[1]['day'] - 16)*72
        hour = (u[1]['hour'])*3
        min = (u[1]['minute'])%3

        ulti_twentyMins[day+hour+min]+=1



    # create array for every 20 minutes from 10-16 00:00 to 10-20 00:00
    natty_twentyMins = np.zeros(288)

    for u in nattys.iterrows():
        day = (u[1]['day'] - 16)*72
        hour = (u[1]['hour'])*3
        min = (u[1]['minute'])%3
        
        natty_twentyMins[day+hour+min]+=1

    sns.set(style='darkgrid', context='poster')
    plt.figure(figsize=(20,15))


    s = sns.tsplot(ulti_twentyMins, color="hls")
    s = sns.tsplot(natty_twentyMins, color="Set2")
    s.set_ylabel("Tweets")
    s.set_title("Tweets per Twenty Minutes")
    s.set_xticks([72, 144, 216, 287])
    s.set_xticklabels(['17th', '18th', '19th', '20th'])
    s.set_xlabel("Day")


    s.figure.savefig("ByTwenty.png")





# parse data into nice format
ultilive = parseData('ultilive')
nattys = parseData('nattys')

# plot tweets per hour
#barplotHours(ultilive, nattys)

# scatterplot of tweets throughout the time
twentyMins(ultilive, nattys)

