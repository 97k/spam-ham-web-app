import string
from nltk.corpus import stopwords


def text_process(message):
    noPunc = [char for char in message if char not in string.punctuation]
    noPunc = ''.join(noPunc)

    return [word for word in noPunc.split() if word not in stopwords.words('english')]
