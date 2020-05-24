import os

import nltk
# nltk.download('punkt')
import pandas as pd


class ArticleCSVParser:

    def transform_texts_to_df(self, name: str, genre_list: list, delimiter: str = '\t') -> pd.DataFrame:
        article_df_list = list()
        for genre in genre_list:
            article_df_list.append(self.extract_genre_files(genre))
        df = pd.concat(article_df_list)
        df.to_csv(name, sep=delimiter)
        return df

    def extract_genre_files(self, genre: str) -> pd.DataFrame:
        found = True
        current_number = 1
        titles = list()
        subtitles = list()
        texts = list()
        token_counts = list()
        while found:
            file_name = "{:03d}.txt".format(current_number)
            text_data = self.read_and_split_file(genre, file_name)
            if len(text_data) != 0:
                titles.append(text_data[0])
                subtitles.append(text_data[1])
                article_text = ' '.join(text_data[2:])
                texts.append(article_text)
                token_counts.append(len(nltk.word_tokenize(article_text)))
                current_number += 1
            else:
                found = False

        genres = [genre] * len(titles)
        data = {'genre': genres, 'title': titles, 'subtitle': subtitles, 'text': texts, 'token_counts': token_counts}
        data_frame = pd.DataFrame(data)
        return data_frame

    def read_and_split_file(self, genre: str, file_name: str) -> list:
        text_data = list()
        current_file = os.path.abspath(os.path.join('data', genre, file_name))
        if os.path.exists(current_file):
            open_file = open(current_file, 'r', encoding="latin-1")
            text_data = open_file.read().split('\n')
            text_data = list(filter(None, text_data))
        return text_data
