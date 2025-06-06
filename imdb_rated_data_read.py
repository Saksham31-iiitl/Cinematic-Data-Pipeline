import pandas as pd

file_path = 'IMDb_top_rated_data.csv'
df = pd.read_csv(file_path)

df['genres'] = df['genres'].str.strip().str.rstrip(',')
df_genres = df.assign(genres=df['genres'].str.split(',')).explode('genres')
df_genres['genres'] = df_genres['genres'].str.strip()


df_genres['releaseYear'] = pd.to_datetime(df_genres['releaseYear'], format='%Y')


df_genres['decade'] = (df_genres['releaseYear'].dt.year // 10) * 10


df_genres.columns = df_genres.columns.str.lower().str.replace(' ', '_')


print(df_genres.head())
print(df_genres.info())
print(df_genres.describe())
