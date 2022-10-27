# -*- coding: utf-8 -*-
"""Stock-price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-diWfZ5bSnx9pFn4DP9P1DCPAoVvgpL-
"""
#%%
import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt

import keras.api._v2.keras as keras

from keras import layers
from keras import Adam
from keras import Sequential



# CSV was downloaded from https://finance.yahoo.com/quote/PYPL?p=PYPL&.tsrc=fin-srch -> provides data such as what the stock opened at, What the high and low price was and what the stock closed at. I will be using the date and what the stock closed at for that date.

# Note: The Vs code extension 'Jupyter' is very useful, and is what I used during the course of this project.

#TODO: currently the graph is set up to recieve data from downloaded .csv files. in the future I would like to redesign this to recieve data via links and still export graphs

df = pd.read_csv('PYPL.csv') 
df

#filters the data from the csv and shows only The closing price and the date
df = df[['Date', 'Close']]
df

# converts a string to a date i.e "2015-07-06"
def str_to_datetime(dateString):
  split = dateString.split('-')
  year,month,day = int(split[0]),int(split[1]),int(split[2])

  return datetime.datetime(year=year,month=month, day=day)
datetime_object = str_to_datetime('2015-07-06')
datetime_object

df['Date'] = df['Date'].apply(str_to_datetime)
df['Date']

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

def x_y_df(data_window):
  # converts the time window into a numpy array
  # We covert this because we are able to push the data to the training model.
  df_as_np = data_window.to_numpy()

  dates = df_as_np[:, 0]

  middle_matrix = df_as_np[:, 1:-1]

  # Number of obseravtions / how many number of columns (close) / 1 variable
  X = middle_matrix.reshape((len(dates), middle_matrix.shape[1], 1))
  # only get the last column
  Y = df_as_np[:, -1]


  return dates, X.astype(np.float32), Y.astype(np.float32)

dates, X, y = x_y_df(df_time_between)

dates.shape, X.shape, y.shape

# Number of results, 3 columns (target 1 - 3), 1 type of variable (close)

dates_times_8 = int(len(dates) * .8)
dates_times_9 = int(len(dates) * .9)

# first train uses 80% of the dates
dates_train, X_train, y_train = dates[:dates_times_8], X[:dates_times_8], y[:dates_times_8]

# first validation uses 90% of the dates
dates_val, X_val, y_val = dates[dates_times_8:dates_times_9], X[dates_times_8:dates_times_9], y[dates_times_8:dates_times_9]
# first testing uses 90% of the dates
dates_test, X_test, y_test = dates[dates_times_9:], X[dates_times_9:], y[dates_times_9:]

# This is the data that was used to train 
plt.plot(dates_train, y_train) 
# Validation is the data that has matched with the prediction
plt.plot(dates_val, y_val)
# Test is the prediction the computer has made
plt.plot(dates_test, y_test)

# training = blue
# validation = orange
# test = green
plt.legend(['Training', 'Validated', 'Test prediction'])

model = Sequential([layers.Input((3, 1)), layers.LSTM(32), layers.Dense(16, activation='relu'), layers.Dense(16, activation='relu'), layers.Dense(1)])
# 0.001 -> learning rate
# M.A.R -> avg we are wrong by
model.compile(loss='mse', optimizer=Adam(learning_rate=0.001),metrics=['mean_absolute_error'])

#Epochs -> how many times it runs through the data
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50)

training= model.predict(X_train).flatten()

plt.plot(dates_train, training)
plt.plot(dates_train, y_train)

# Blue -> What the program believed would happen / it follows the data it was trained on
# Orange -> what really happened / what the program saw happened
plt.legend(['Training Predictions', 'Training Observations'])

val_predictions = model.predict(X_val).flatten()

plt.plot(dates_val, val_predictions)
plt.plot(dates_val, y_val)
plt.legend(['Validation Predictions', 'Validation Observations'])

test_predictions = model.predict(X_test).flatten()

plt.plot(dates_test, test_predictions)
plt.plot(dates_test, y_test)
plt.legend(['Testing Predictions', 'Testing Observations'])

# Combine all the previous graphs into 1 final graph

plt.plot(dates_train, training)
plt.plot(dates_train, y_train)
plt.plot(dates_val, val_predictions)
plt.plot(dates_val, y_val)
plt.plot(dates_test, test_predictions)
plt.plot(dates_test, y_test)
plt.legend(['Training Predictions', 'Training Observations','Validation Predictions', 'Validation Observations', 'Testing Predictions', 'Testing Observations'])

# Orange -> Follow the data in the training 
# Red -> what actually happened
# Green -> What it thought happened
# Brown -> what really happened
# Purple -> what really happened
# The model might be able to predict the future, but it is not able to predict the future with 100% accuracy. 

# %%
