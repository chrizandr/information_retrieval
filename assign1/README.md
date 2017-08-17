# Assignment 1

Given a large corpus of documents create an index table for the words in each document and retrieve the list of documents matching a given query.

### Steps to run

Download the data from [here](http://www.isical.ac.in/~fire/data/docs/adhoc/en.docs.2011.tar.gpg)

Extract the data folders, you may need a paraphrase to decrypt the file. Please email [here](mailto:amitava.das@iiits.in) for one.

Create a data folder in the same directory as the source code, this is where the documents will be stored
```bash
mkdir data
```
The corpus is extremely large, it is advised to use only a subset of the corpus.
We use `file_handle.py` for this. Change parameters in `file_handle.py`
```python

corpus_size = 5000      # The number of documents you want in the subset corpus
data_path = "path/to/extracted/data/folders"

format_files(root_path=data_path, n=corpus_size)
```
Run `file_handle.py`

```bash
python file_handle.py
```
File handler creates a subset corpus in the `data` folder, with each document formatted and labelled with an ID.

We will now build the index for our subset corpus.
Build the index using `index.py`
```bash
python index.py
```

Once the index is built we can run queries on the corpus
Search the corpus using the built index with `search.py`
```python
from search import search

doc_ids = search("Eiffel Tower")
print(doc_ids)
```

This will give IDs of all documents that have the words `Eiffel` and `Tower` in them.
