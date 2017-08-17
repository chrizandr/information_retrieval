"""Main file."""

import nltk
from nltk.stem.snowball import SnowballStemmer
import pickle
import os


def tokenize(data):
    """Given the file string return the tokenized words."""
    return nltk.word_tokenize(data)


def stem(words):
    """Stem the list of words."""
    stemmer = SnowballStemmer("english")
    new_words = [stemmer.stem(x) for x in words]
    return new_words


def create_index_table():
    """Create the index table for the words in the corpus."""
    index = dict()
    files = os.listdir("data/")
    for f in files:
        print("Processing", f)
        with open("data/" + f, 'r') as myfile:
            data = myfile.read()
            words = stem(tokenize(data))
            for word in words:
                try:
                    index[word].append(int(f[0:-4]))
                except KeyError:
                    index[word] = [int(f[0:-4])]
    f = open("index.pkl", "wb")
    pickle.dump(index, f)
    f.close()


if __name__ == "__main__":
    create_index_table()
