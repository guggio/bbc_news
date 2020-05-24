import os

import pandas as pd
from sklearn.model_selection import train_test_split


def create_absolute_path(*paths):
    paths = "/".join(paths)
    return os.path.abspath(paths)


data_dir = create_absolute_path('..', 'generated_data')
data_path = create_absolute_path(data_dir, 'bbc_articles.csv')
df = pd.read_csv(data_path, sep='\t')
df_text_genre = df[['text', 'genre']]
df_text_genre = df_text_genre.sample(frac=1).reset_index(drop=True)
train, test = train_test_split(df_text_genre, test_size=0.2, random_state=42, shuffle=True)
train_path = create_absolute_path(data_dir, 'train.tsv')
test_path = create_absolute_path(data_dir, 'test.tsv')
train.to_csv(train_path, sep='\t', index=False)
test.to_csv(test_path, sep='\t', index=False)
