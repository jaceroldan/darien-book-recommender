import ast
import pandas as pd

from flask import Flask 
from flask_cors import CORS

app =  Flask(__name__)
CORS(app)

categories = ['Fiction', 'Comics & Graphic Novels', 'Comedy', 'Biography & Autobiography', 'Cooking']
authors = ['Neal Stephenson', 'Bill Watterson', 'Harpo Marx', 'John Perkins']

@app.route("/")
def recommend():
    book_data = pd.read_csv('books_data.csv')

    # Ensure that the response has an image
    book_data = book_data[book_data['image'].isna() == False]

    # Ensure that the response has a category
    book_data = book_data[book_data['categories'].isna() == False]

    # Ensure that the response has an author
    book_data = book_data[book_data['authors'].isna() == False]

    book_data['first_category'] = book_data['categories'].apply(lambda x: ast.literal_eval(x)[0])

    book_data['first_author'] = book_data['categories'].apply(lambda x: ast.literal_eval(x)[0])

    # Match categories
    categories_book_data = book_data[book_data['first_category'].isin(categories) == True]

    # Match authors
    authors_book_data = book_data[book_data['first_author'].isin(authors) == True]

    # combined dataset
    filtered_book_data = pd.concat([categories_book_data, authors_book_data])

    sample = filtered_book_data.sample().to_json()
    return sample
