import nltk
import numpy as np
import random
import string # to process standard python strings

f=open('./cornell_move_corpus/movie_lines.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()# converts to lowercase
nltk.download('punkt') # first-time use only
nltk.download('wordnet') # first-time use only
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
print(sent_tokens[0]) 
word_tokens = nltk.word_tokenize(raw)# converts to list of words
print(word_tokens[0])
