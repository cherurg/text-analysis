import tfidf
from os import listdir
from os.path import isfile, join
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import nltk
import string
from nltk.corpus import stopwords
stopwords = stopwords.words('russian')
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[^\W\d]+((?:[^\W\d]|[-'])+[^\W\d]+)*")

mypath = '../corpus/content/'
files = [ mypath + f for f in listdir(mypath) if isfile(join(mypath,f)) ]

files_content = []
table = tfidf.tfidf()
for file in files[:100]:
    files_content.append({})
    files_content[-1]['tokens'] = []
    files_content[-1]['words'] = []
    lines = open(file, 'rb')
    for line in lines:
        tokenized_line = tokenizer.tokenize(line.decode('utf-8').strip())
        for token in tokenized_line:
            if not token in string.punctuation:
                files_content[-1]['tokens'].append(token.lower())
                files_content[-1]['words'].append(morph.parse(token)[0].normal_form)

    table.addDocument(file, files_content[-1]['words'])
