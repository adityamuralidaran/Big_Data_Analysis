#!/usr/bin/python

# Aditya Subramanian Muralidaran


import sys
import nltk
import string

nltk.download('tokenize')
nltk.download('RegexpTokenizer')
from nltk.tokenize import RegexpTokenizer

nltk.download('stopwords')
nltk.download('corpus')
nltk.download('words')

for ipdata in sys.stdin:
	stop_words = nltk.corpus.stopwords.words('english')
	data_lower = ipdata.lower();
	tokenizer = RegexpTokenizer(r'\w+')
	word_list = tokenizer.tokenize(data_lower)
	for x in word_list:
		if x not in stop_words and x.isalpha() and len(x)>2:
			print (x+"\t"+str(1))