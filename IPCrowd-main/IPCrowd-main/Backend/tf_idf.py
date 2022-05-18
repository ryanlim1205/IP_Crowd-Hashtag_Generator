def sort_matrix(temp_matrix):
    """Sort a dict with the highest score"""

    tuples = zip(temp_matrix.col, temp_matrix.data)

    return sorted(tuples, key = lambda x: (x[1], x[0]), reverse = True)

def extract_num_from_vector(feature_names, sorted_items, top_num = 5):
    """get feature names and tf-idf scores of top 5 items"""

    # only use top 5 items from vector
    sorted_items = sorted_items[:top_num]

    scores = []
    features = []

    for index, score in sorted_items:
        scores.append(round(score, 3))
        features.append(feature_names[index])

    result = {}
    for idx in range(len(features)):
        result[features[idx]] = scores[idx]
    
    return result

def get_hashtags(vectorizer, feature_names, inputs):
    """Return hashtags from user input"""

    # generate tf-idf for the user input
    tf_idf_vector = vectorizer.transform([inputs])

    # sort the tf-idf vectors in decreasing order of scorces
    sorted_items = sort_matrix(tf_idf_vector.tocoo())

    # generate hashtags
    hashtags = extract_num_from_vector(feature_names, sorted_items, 5)

    return list(hashtags.keys())