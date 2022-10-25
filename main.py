
#%%
import pandas as pd
import datetime
import matplotlib.pyplot as plt
# CSV was downloaded from https://finance.yahoo.com/quote/PYPL?p=PYPL&.tsrc=fin-srch -> provides data such as what the stock opened at, What the high and low price was and what the stock closed at. I will be using the date and what the stock closed at for that date.
# Note: The Vs code extension 'Jupyter' is very useful, and is what I used during the course of this project.
df = pd.read_csv('PYPL.csv') 



df

df = df[['Date', 'Close']]
df

def str_to_datetime(s):
  split = s.split('-')
  year,month,day = int(split[0]),int(split[1]),int(split[2])

  return datetime.datetime(year=year,month=month, day=day)
datetime_object = str_to_datetime('2015-07-06')
datetime_object

df.index = df.pop('Date')
df

plt.plot(df.index, df['Close'])

# %%