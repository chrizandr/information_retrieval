"""Handle searches for different queries."""

from index import tokenize, stem
import pickle


def load_index(pickle_path):
    """Load the index file."""
    f = open(pickle_path, "rb")
    index = pickle.load(f)
    return index


def search(query):
    """Search the index for the given query."""
    index = load_index("index.pkl")
    words = stem(tokenize(query))
    for word in words:
        doc_set = set()
        try:
            word_doc_set = set(index[word])
            doc_set = doc_set.union(word_doc_set)
        except KeyError:
            pass
    return list(doc_set)


if __name__ == "__main__":
    print(search("My name is Chris"))
