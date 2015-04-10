import pandas as pd
import datetime as dt
import matplotlib as mp
from pandas.tseries.offsets import *
import seaborn as sns



# read csv
ultilive = pd.read_csv('data/ultilive.csv', parse_dates=['Posted at'])

# change index
ultilive.set_index('Posted at', inplace = True)

ultilive.index = ultilive.index - DateOffset(hours=5)

# cut out screen name and id
ultilive = ultilive[['Text']]

# add dates
ultilive['month'] = ultilive.index.month
ultilive['day'] = ultilive.index.day
ultilive['hour'] = ultilive.index.hour
ultilive['minute'] = ultilive.index.minute


# sort
ultilive = ultilive.sort_index(ascending=True)

start = ultilive.index.searchsorted(dt.datetime(2014, 10, 16))
end = ultilive.index.searchsorted(dt.datetime(2014, 10, 20))

ultilive = ultilive.ix[start:end]

hours = ultilive.groupby('hour')
sns.barplot(hours, hours.size())
