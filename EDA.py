import pandas as pd
import numpy as np

def load_data(file_path):
    books = pd.read_csv(file_path)
    return books

def clean_date(df, date_column):
    df[date_column] = df[date_column].str.replace('"','',regex=False)
    return df

def date_to_datetime(df, date_column):
    df[date_column] = pd.to_datetime(df[date_column], dayfirst=True, errors='coerce')
    return df

def save_as_csv(df):
    df.to_csv('data/cleaned_books2.csv', index=False)

def date_difference(df, column1, column2, new_column):
    df[new_column] = (df[column2] - df[column1]).dt.days
    return df

def drop_na_for_column(df, ID_column):
    df = df.dropna(subset=[ID_column])
    return df

def clean_string(df, string_column):
    df[string_column] = df[string_column].str.strip().str.title()
    return df

books = load_data("data/03_Library Systembook.csv")
books = drop_na_for_column(books, 'Id')
books = clean_string(books, 'Books')
books = clean_date(books, 'Book checkout')
books = date_to_datetime(books, 'Book checkout')
books = date_to_datetime(books, 'Book Returned')
books = date_difference(books, 'Book checkout', 'Book Returned', 'Time on Loan')
save_as_csv(books)



