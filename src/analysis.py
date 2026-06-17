import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("data/spotifysongs.csv")
print(df.isnull().sum())
df = df.dropna()
print(df.duplicated().sum())
df = df.drop_duplicates()
"""
# to find popular songs
top_songs = df.sort_values(
    by="popularity",
    ascending=False
)

print(top_songs.head(10))
#to find most common artists
print(
    df["artists"].value_counts().head(10)
)
top_artists = df["artists"].value_counts().head(10)

top_artists.plot(kind="bar")

plt.title("Top Artists")

plt.show()
"""
df['x']= df['danceability']-df['acousticness']
df['y']=df['energy']-df['valence']
sizes= df['popularity']/5
plt.figure(figsize=(12,8))
plt.scatter(df['x'],df['y'],s=sizes,alpha=0.08)

plt.title("Orbitfy")
plt.xlabel("Acoustiness ← → Danceable")
plt.ylabel("Calm ← → Intense")
plt.show()
