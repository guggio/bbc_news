import os

import pandas as pd
from sklearn.model_selection import train_test_split


def create_absolute_path(*paths):
    paths = "/".join(paths)
    return os.path.abspath(paths)


# first create a path variable to access the data and save the train and test files
# Due to my file structure I use '..' to go back one level (to the main project level)
# in order to access my generated_data folder.
# In this directory I store my main data set and want to use it to store my train and test set.
data_dir = create_absolute_path('..', 'generated_data')

# create a path variable to the data set and read the data
data_path = create_absolute_path(data_dir, 'bbc_articles.csv')
df = pd.read_csv(data_path, sep='\t')

# select the wanted columns
df_text_genre = df[['text', 'genre']]
# shuffle the rows
df_text_genre = df_text_genre.sample(frac=1).reset_index(drop=True)

# split the data into train and test set
train, test = train_test_split(df_text_genre, test_size=0.2, random_state=42, shuffle=True)

# determine the path where to save the train and test file
train_path = create_absolute_path(data_dir, 'train.tsv')
test_path = create_absolute_path(data_dir, 'test.tsv')

# save the train and test file
train.to_csv(train_path, sep='\t', index=False)
test.to_csv(test_path, sep='\t', index=False)
