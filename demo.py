import pandas as pd
import numpy as np

tables=pd.read_html("https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29")

df=tables[3]

# table_3.columns=range(table_3.shape[1])
df.columns=range(df.shape[1])
df=df[[0,2]]

df=df.iloc[1:11,:]

df.columns=['Country','GDP (MILLION USD)']

df['GDP (MILLION USD)']=df['GDP (MILLION USD)'].astype(int)
df['GDP (MILLION USD)']=df[['GDP (MILLION USD)']]/1000
df['GDP (MILLION USD)']=np.round(df['GDP (MILLION USD)'],2)
df.rename(columns={"GDP (MILLION USD)":"GDP (BILLION USD)"},inplace=True)

df.to_csv("Largest_economies.csv")