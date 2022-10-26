#%%
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
# import tensorflow as tf
# CSV was downloaded from https://finance.yahoo.com/quote/PYPL?p=PYPL&.tsrc=fin-srch -> provides data such as what the stock opened at, What the high and low price was and what the stock closed at. I will be using the date and what the stock closed at for that date.

# Note: The Vs code extension 'Jupyter' is very useful, and is what I used during the course of this project.

#TODO: currently the graph is set up to recieve data from downloaded .csv files. in the future I would like to redesign this to recieve data via links and export graphs

df = pd.read_csv('PYPL.csv') 
# df

#filters the data from the csv and shows only The closing price and the date
df = df[['Date', 'Close']]
# df

# converts a string to a date i.e "2015-07-06"
def str_to_datetime(dateString):
  split = dateString.split('-')
  year,month,day = int(split[0]),int(split[1]),int(split[2])

  return datetime.datetime(year=year,month=month, day=day)
datetime_object = str_to_datetime('2015-07-06')
datetime_object

df['Date'] = df['Date'].apply(str_to_datetime)
# df['Date']

# Replaces the index of the chart with the date instead
df.index = df.pop('Date')
df

# Plots a graph by the close price, using matplotlib
plt.plot(df.index, df['Close'])


# LSTM

# select 2 dates from the stock that will be used for testing data 
def time_between(dataframe, first_day, last_day, n=3):
  first_day = str_to_datetime(first_day)
  last_day  = str_to_datetime(last_day)

  date_to_target = first_day
  
  dates = []
  X, Y = [], []

  previous = False
  while True:
    df_subset = dataframe.loc[:date_to_target].tail(n+1)
    
    if len(df_subset) != n+1:
      print('the time window you set is too big')
      return

    results = df_subset['Close'].to_numpy()
    x, y =results[:-1],results[-1]

    dates.append(date_to_target)
    X.append(x)
    Y.append(y)

    next_week = dataframe.loc[date_to_target : date_to_target + datetime.timedelta(days=7)]

    next_datetime_str = str(next_week.head(2).tail(1).index.values[0])

    next_date_str = next_datetime_str.split('T')[0]

    year_month_day = next_date_str.split('-')
    year, month, day = year_month_day

    next_date = datetime.datetime(day=int(day), month=int(month), year=int(year))
    
    if previous:
      break
    
    date_to_target = next_date

    if date_to_target ==last_day:
      previous = True
    
  new_df = pd.DataFrame({})
  new_df['Target Date'] = dates
  
  X = np.array(X)
  for i in range(0, n):
    X[:, i]
    new_df[f'Target-{n-i}'] = X[:, i]
  
  new_df['Target'] = Y

  return new_df

# We will now provide dateframe, time frame, and how many target results (3)
df_time_between = time_between(df, '2015-10-08', '2022-10-24', n=3)
df_time_between

# %%
