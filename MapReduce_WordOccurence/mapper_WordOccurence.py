#!/usr/bin/python



import sys
import nltk
import string

nltk.download('tokenize')
nltk.download('RegexpTokenizer')
from nltk.tokenize import RegexpTokenizer

nltk.download('stopwords')
nltk.download('corpus')
nltk.download('words')

# top words for News data
top_words = ['shooting','gun','attack','said','police','officers','school','killed','people','shot']

# top words for Twitter data
#top_words = ['gun','shooting','attack','voilence','school','survivor','people','police','parkland','survived']

for ipdata in sys.stdin:
	stop_words = nltk.corpus.stopwords.words('english')
	data_lower = ipdata.lower();
	tokenizer = RegexpTokenizer(r'\w+')
	word_list = tokenizer.tokenize(data_lower)
	filter_word_list = list(filter(lambda x: x not in stop_words and len(x) > 2 and x.isalpha(),word_list))
	for i in range(len(filter_word_list)-1):
		x = filter_word_list[i]
		if x in top_words:
			print ("<"+x+","+filter_word_list[i+1]+">\t"+str(1))