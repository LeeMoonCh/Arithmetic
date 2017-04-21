# coding:utf8

import nltk

print nltk.corpus.gutenberg.fileids()





words = nltk.corpus.cmudict.entries()
for word in words:
    word