import pandas as pd
# CSV was downloaded from https://finance.yahoo.com/quote/PYPL?p=PYPL&.tsrc=fin-srch -> provides data such as what the stock opened at, What the high and low price was and what the stock closed at. I will be using the date and what the stock closed at for that date.
df = pd.read_csv('PYPL.csv') 



df