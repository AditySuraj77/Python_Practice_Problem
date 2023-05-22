from sklearn.feature_extraction.text import CountVectorizer


def bag_word(string):
    vectorizer = CountVectorizer()

    vector = vectorizer.fit_transform(string)

    return vector.toarray()


user_string = ['I Love Coding',
               'Be Aware with AI',
               'Quit is not an option'

]

result = bag_word(user_string)
print(result)
