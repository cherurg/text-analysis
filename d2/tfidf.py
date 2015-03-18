#!/usr/bin/env python

"""
The simplest TF-IDF library imaginable.

Add your documents as two-element lists `[docname, [list_of_words_in_the_document]]` with `addDocument(docname, list_of_words)`. Get a list of all the `[docname, similarity_score]` pairs relative to a document by calling `similarities([list_of_words])`.

See the README for a usage example.
"""

import sys
import os
import math

class tfidf:
  def __init__(self):
    self.weighted = False
    self.documents = {}
    self.corpus_dict = {}
    self.__vectors = {}

  def addDocument(self, doc_name, list_of_words):
    # building a dictionary
    doc_dict = {}
    for w in list_of_words:
      doc_dict[w] = doc_dict.get(w, 0.) + 1.0
      self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

    # normalizing the dictionary
    length = float(len(list_of_words))
    for k in doc_dict:
      doc_dict[k] = doc_dict[k] / length

    # add the normalized document to the corpus
    self.documents[doc_name] = doc_dict

  def tf(self, word, doc_name):
    doc = self.documents.get(doc_name, {})
    if len(doc) == 0:
      return 0.

    words_number = 0.0
    for w, count in doc.items():
      words_number += count

    return doc.get(word, 0)/words_number

  def idf(self, word):
    D = len(self.documents)
    count = 0.
    for doc_name, doc in self.documents.items():
      if word in doc:
        count += 1.

    return math.log(D/count)

  def tfidf(self, word, doc_name):
    return self.tf(word, doc_name) * self.idf(word)

  def vector(self, doc_name):
    tfidfs = self.__vectors.get(doc_name, [])
    if len(tfidfs) != 0:
      return tfidfs

    words_list = sorted(self.corpus_dict.keys())
    doc = self.documents[doc_name]

    for word in words_list:
      word_value = doc.get(word, 0.)
      tfidfs.append(self.tf(word, doc_name) * self.idf(word))

    self.__vectors[doc_name] = tfidfs

    return tfidfs

  def vectors(self):
    for doc in self.documents:
      self.vector(doc)

    return self.__vectors

  def cos(self, d1_name, d2_name):
    self.vectors()
    d1 = self.__vectors[d1_name]
    d2 = self.__vectors[d2_name]

    numerator = 0.
    denum1 = 0.
    denum2 = 0.
    words_count = len(d1)
    for i in range(0, words_count):
      numerator += d1[i]*d2[i]
      denum1 += d1[i]*d1[i]
      denum2 += d2[i]*d2[i]

    return numerator/(math.sqrt(denum1) * math.sqrt(denum2))



