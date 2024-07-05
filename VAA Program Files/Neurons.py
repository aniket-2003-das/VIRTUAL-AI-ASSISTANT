import numpy
import nltk 
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,words):
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = numpy.zeros(len(words),dtype=numpy.float32)
    for idx , w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1
    return bag
