import pandas as pd
import numpy as np

class BookClean:

    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    def drop_na_for_column(self, ID_column):
        self.na_rows = self.df[self.df[ID_column].isna()].copy()
        self.na_ID_count = len(self.na_rows)
        self.na_ID_count_df = pd.DataFrame({'NA ID Count' : [self.na_ID_count]})
        self.df = self.df.dropna(subset=[ID_column])
        return self

    def clean_string(self, string_column):
        self.df[string_column] = self.df[string_column].str.strip().str.title()
        return self

    def clean_date(self, date_column):
        self.df[date_column] = self.df[date_column].str.replace('"','',regex=False)
        return self

    def date_to_datetime(self, date_column):
        self.df[date_column] = pd.to_datetime(self.df[date_column], dayfirst=True, errors='coerce')
        return self

    def date_difference(self, column1, column2, new_column):
        self.df[new_column] = (self.df[column2] - self.df[column1]).dt.days
        return self

    def drop_nas(self):
        self.any_nas = self.df.loc[self.df.isna().any(axis=1)]
        self.df = self.df.dropna()
        return self

    def save_as_csv(self, new_file_path):
        self.df.to_csv(new_file_path, index=False)
        return self

    def save_NA_ID_csv(self, NA_ID_file_path):
        self.na_ID_count_df.to_csv(NA_ID_file_path, index=False)
        return self

    def save_NA_any_csv(self, NA_any_file_path):
        self.any_nas.to_csv(NA_any_file_path, index=False)

    def main(self):
        (books.drop_na_for_column('Id')
          .clean_string('Books')
          .clean_date('Book checkout')
          .date_to_datetime('Book Returned')
          .date_to_datetime('Book checkout')
          .date_difference('Book checkout','Book Returned','Time on Loan')
          .drop_nas()
          .save_as_csv('data/cleaned_books3.csv')
          .save_NA_ID_csv('data/books_NA_IDs.csv')
          .save_NA_any_csv('data/books_NA_any.csv'))
        
if __name__ == "__main__":

    books = BookClean("data/03_Library Systembook.csv")
    books.main()
