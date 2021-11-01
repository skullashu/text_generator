# import dependencies

import numpy
import sys
install nltk
nltk.downloads('stopwords')
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint

#Load data
file = open("frankenstein-2.txt").read()

# tokenization
# standardization
def tokenize_words(input):
  input = input.lower()
  tokenizer = RegexpTokenizer(r'\w+')
  tokens = tokenizer.tokenize(input)
  filtered = filter(lambda token: token not in stopwords.words('english'), tokens)
  return "".join(filtered)
processed_inputs = tokenize.words(file)


  
