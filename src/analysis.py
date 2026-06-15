import pandas as pd
df= pd.read_csv("data/spotifysongs.csv")
print(df.head())
print (df.info())
print(df.isnull().sum())
df = df.dropna()
print(df.duplicated().sum())
df = df.drop_duplicates()

