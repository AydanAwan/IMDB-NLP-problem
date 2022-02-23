# IMDB-NLP-problem

Problem Statement:
Implement a movies recommender system based on movies synopses. The principle is to use movie 
synopses to automatically identify other movies similar to the ones the user likes. How? by using 
natural language processing.
This recommender system is built on an item-based method, also called content-based method, for 
which the similarity between items (in our case, movies) is exploited. The recommender system 
identifies movies that the user has highly rated in the past, and then suggests movies very similar to 
its tastes and preferences

Steps:
1- Pre-processing the synopses: First of all, remove punctuations and irrelevant words like 
stop words and persons’ names.
2- Creating the dictionary: The dictionary consists of a concatenation of unique words of all 
synopses.
3- Creating the corpus: The corpus is the collection of all synopses pre-processed and 
transformed using the dictionary.
4- Creating the tf-idf transformation: The term frequency-inverse document frequency (tf-idf) 
transformation reflects the importance of words in the corpus. The (tf-idf) value of a word 
depends not only on the word count in a document, but also on the number of occurrences 
in the corpus.
5- Choice of the number of topics: As mentioned above, LSA seeks to identify a set of topics 
related to the movies synopses. The number of these topics N is equal to the dimension of 
the approximation matrix resulting from the SVD dimension reduction technique. This 
number is a hyper-parameter to be carefully adjusted. It results from the selection of the N 
largest singular values of the tf-idf corpus matrix.
6- Creating the LSA model
7- Computation of the similarity between synopses

todo list
- write module tests for each of the steps
- create the modules for transforming the data so using nltk to tokenize and remove stop words, punctuation and names and TextBlob to refine it
- create the dictionary using gensim
- create the corpus from the dictionary using gensim
- 