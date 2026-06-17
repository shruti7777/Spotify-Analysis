import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
df = pd.read_csv("data/spotifysongs.csv")
df = df.dropna()
features =['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
print(df.columns)