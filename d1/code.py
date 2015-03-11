from __future__ import unicode_literals
from sets import Set
from collections import Counter
#three line to fix ascii-problem in stopwords
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import nltk
import pymorphy2
import string
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[^\W\d]+((?:[^\W\d]|[-'])+[^\W\d]+)*")
morph = pymorphy2.MorphAnalyzer()

from nltk.corpus import stopwords
stopwords = [sw.decode('utf-8') for sw in stopwords.words('russian')]
#print "Number of stopwords: ", len(stopwords)


lines = open(sys.argv[1]).readlines()
tokens = []
for line in lines:
	tokenized_line = tokenizer.tokenize(line.decode('utf-8').strip())
	for token in tokenized_line:
		if not token in string.punctuation:
			tokens.append(token.lower())

print 'Number of tokens:', len(tokens)
words = nltk.FreqDist(tokens)

print 'Number of words:', len(words)
lemmata = nltk.FreqDist()
for word in words:
	gram_info = morph.parse(word)
	nf = gram_info[0].normal_form
	lemmata[nf] += words[word]

print 'Number of lemmas:', len(lemmata)

atricle_words = [word[0] for word in words.most_common()]
atricle_words = Set(atricle_words)
stopwords = Set(stopwords)

print "\nNumber of words without stopwords: ", len(atricle_words - stopwords)
print "Number of lemmas without stopwords: ", len(Set(lemmata) - stopwords)


#the most frequent nouns
nouns = []
for token in tokens:
	parsed_token = morph.parse(token)[0]
	if 'NOUN' in parsed_token.tag:
		norm = parsed_token.normal_form
		nouns.append(norm)

nouns = nltk.FreqDist(nouns)
for noun in nouns.most_common()[:10]:
	print(noun[0])
	print(noun[1])
	print(float(noun[1])/len(tokens))
	print('\n')
