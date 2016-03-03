__author__ = 'oger'

import sys
import numpy as np
import numpy.matlib
from gensim import corpora, models
reload(sys)
sys.setdefaultencoding('utf-8')

corpus_tfidf = corpora.MmCorpus('corpus_tfidf.dat')
word_num = corpus_tfidf.num_terms
doc_num = corpus_tfidf.num_docs

feature_size = 100

word2vec = np.matlib.empty((word_num,feature_size))
f = open('id_word2vec.txt', 'r')
while 1:
    line = f.readline()
    if not line:
        break
    line = line.strip('\n')
    if not line:
        continue
    line_val = line.split(' ')
    vector = map(float,line_val[1:])
    id = int(line_val[0])
    word2vec[id] = vector

# ret = np.matlib.empty((doc_num,feature_size))
for i in xrange(corpus_tfidf.num_docs):
    doc_val = np.matlib.zeros((1,5))
    for tfidf_tuple in corpus_tfidf[i]:
        word_id = tfidf_tuple[0]
        word_tfidf_val = tfidf_tuple[1]
        doc_val += word2vec[word_id]* word_tfidf_val
    # ret[i] = doc_val
    for x in list(numpy.array(doc_val).reshape(-1,)):
        print x,
    print