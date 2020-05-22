from article_csv_parser import ArticleCSVParser

if __name__ == "__main__":
    genre_list = ['business', 'entertainment', 'politics', 'sport', 'tech']
    parser = ArticleCSVParser()
    df = parser.transform_texts_to_df('bbc_articles.csv', genre_list)
    print(df.head())
