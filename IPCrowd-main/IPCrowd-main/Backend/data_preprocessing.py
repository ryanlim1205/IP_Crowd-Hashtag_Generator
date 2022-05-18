import re

def get_stopwords(file_path):
    # loading stopwords from the stopwords.txt file

    with open(file_path, 'r', encoding = "cp1252") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)

        return list(frozenset(stop_set))


def clean_text(text):
    # need to clean the existing texts for better generation

    # lowercase them
    text = text.lower()

    # remove punctuations
    punctuations = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    text = "".join([c for c in text if c not in punctuations])

    # remove whitespaces and new lines
    text = re.sub('\s', ' ', text)

    return text