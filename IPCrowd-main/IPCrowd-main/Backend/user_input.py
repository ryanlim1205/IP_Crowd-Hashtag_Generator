import pandas as pd
from scipy import rand
from sklearn.feature_extraction.text import TfidfVectorizer
from data_preprocessing import clean_text, get_stopwords
from tf_idf import get_hashtags
from enter_sentence import add_new_sentence


print("Welcome to the hashtag generator!")
random_sentence = input("Enter any sentence to generate hashtags: ")
list_random_sentence = []
list_random_sentence.append(random_sentence)

add_new_sentence(list_random_sentence)



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

result = []
print(get_hashtags(vectorizer, feature_names, random_sentence))
for sentence in temp_data[0:60]:
    dataset = {}
    dataset['user_input_sentence'] = sentence
    dataset['hashtags'] = get_hashtags(vectorizer, feature_names, sentence)

    # for hashies in dataset['hashtags']:
        # hashies = "#" + hashies
        # print(hashies)

    result.append(dataset)

final_result = pd.DataFrame(result)
#print(final_result)