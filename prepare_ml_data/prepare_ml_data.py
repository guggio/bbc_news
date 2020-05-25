from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

# First create a path variable to access the data and save the train and test files
# Due to my file structure I use '..' to go back one level (to the main project level)
# in order to access my generated_data folder.
# In this directory I store my main data set and want to use it to store my train and test set.
data_dir = Path('..', 'generated_data')

# create a path variable to the data set and read the data
data_path = Path(data_dir, 'bbc_articles.csv')

# the data is stored in a tab-separated values file, we need '\t' as the separator
df = pd.read_csv(data_path, sep='\t')

# select the wanted columns
df_text_genre = df[['text', 'genre']]
# shuffle the rows. This is necessary since the rows are grouped by genre and this could lead to genre imbalances
# in the train or test set.
df_text_genre = df_text_genre.sample(frac=1).reset_index(drop=True)

# split the data into train and test set
train, test = train_test_split(df_text_genre, test_size=0.2, random_state=42, shuffle=True)

# determine the path where to save the train and test file
train_path = Path(data_dir, 'train.tsv')
test_path = Path(data_dir, 'test.tsv')

# save the train and test file
train.to_csv(train_path, sep='\t', index=False)
test.to_csv(test_path, sep='\t', index=False)
