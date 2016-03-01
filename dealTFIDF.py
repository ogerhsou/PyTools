__author__ = 'oger'

import sys
from gensim import corpora, models
reload(sys)
sys.setdefaultencoding('utf-8')

train_set = []

f = open('pureData.txt', 'r')
while 1:
    line = f.readline()
    if not line:    #need
        break
    line=line.strip('\n')
    if not line:
        continue
    word_list = line.split(' ')
    train_set.append(word_list)

dic = corpora.Dictionary(train_set)
corpus = [dic.doc2bow(text) for text in train_set]
tfidf = models.TfidfModel(corpus)

corpus_tfidf = tfidf[corpus]
corpus_tfidf.save('corpus_tfidf.dat')

# t1 = models.TfidfModel.load('corpus_tfidf.dat')