from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from data_preprocessing import clean_text, get_stopwords
from tf_idf import get_hashtags
from enter_sentence import add_new_sentence

app = Flask(__name__)
CORS(app)

# Reading the sentences in the csv (database) file
data = pd.read_csv('texts.csv', encoding = "cp1252")

"""
Making sure that the senteces are read correctly
print(data.to_string())
print(data.head(5))

"""

data.dropna(subset=['user_input_sentence'], inplace = True)
data['user_input_sentence'] = data['user_input_sentence'].apply(clean_text)

temp_data = data['user_input_sentence'].to_list()

# load stopwords
stopwords = get_stopwords("stopwords.txt")

# initialize TF-IDF vectorizer with stopwords
vectorizer = TfidfVectorizer(stop_words = stopwords, smooth_idf = True, use_idf = True)

# creating vocab with our dataset
# exclude first 10 texts for testing purpose
vectorizer.fit_transform(temp_data[5::])

# store hashtags
feature_names = vectorizer.get_feature_names_out()

@app.route('/')
def first():
    return "my world"

@app.route('/gethash', methods=['GET', 'POST'])
def getHashtags():
    random_sentence = "georgia tech is the best school"
    list_random_sentence = []
    list_random_sentence.append(random_sentence)

    add_new_sentence(list_random_sentence)
    return {'sentence': random_sentence ,'hashes': get_hashtags(vectorizer, feature_names, random_sentence)}

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)