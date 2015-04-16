import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from pandas.tseries.offsets import *
import seaborn as sns

# sns settings
sns.set(style="darkgrid", context="talk")



# read csv
ultilive = pd.read_csv('data/ultilive.csv', parse_dates=['Posted at'])

# change index
ultilive.set_index('Posted at', inplace = True)

# timezone change
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

# slice data
start = ultilive.index.searchsorted(dt.datetime(2014, 10, 16))
end = ultilive.index.searchsorted(dt.datetime(2014, 10, 20))
ultilive = ultilive.ix[start:end]

# get hours stats
hours = ultilive.groupby('hour')

# plot valuse
x_hours = np.array(sorted(ultilive.hour.unique()))
y_values = np.array(hours.size())
# plot of hours
sns.barplot(x_hours, y_values, palette="Set2")






