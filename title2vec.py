__author__ = 'oger'

import numpy as np
from numpy import mat
import numpy.matlib
import math
from collections import defaultdict
from six import iteritems
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def unitvec(vec):
    """
    Scale a vector to unit length. The only exception is the zero vector, which
    is returned back unchanged.

    Output will be in the same format as input (i.e., gensim vector=>gensim vector).
    """
    try:
        first = next(iter(vec))     # is there at least one element?
    except:
        return vec

    if isinstance(first, (tuple, list)) and len(first) == 2: # gensim sparse format?
        length = 1.0 * math.sqrt(sum(val ** 2 for _, val in vec))
        assert length > 0.0, "sparse documents must not contain any explicit zero entries"
        if length != 1.0:
            return [(termid, val / length) for termid, val in vec]
        else:
            return list(vec)
    else:
        raise ValueError("unknown input type")


def df2idf(docfreq, totaldocs, log_base=2.0, add=0.0):
    """
    Compute default inverse-document-frequency for a term with document frequency `doc_freq`::

      idf = add + log(totaldocs / doc_freq)
    """
    return add + math.log(1.0 * totaldocs / docfreq, log_base)

def precompute_idfs(wglobal, dfs, total_docs):
    """Precompute the inverse document frequency mapping for all terms."""
    # not strictly necessary and could be computed on the fly in TfidfModel__getitem__.
    # this method is here just to speed things up a little.
    return dict((termid, wglobal(df, total_docs))
                for termid, df in iteritems(dfs))


def print_title_vec(sub, vector):
    doc_val = np.matlib.zeros((1,feature_size))
    for tfidf_tuple in vector:
        word = tfidf_tuple[0]
        word_tfidf_val = tfidf_tuple[1]
        doc_val += word2vec[word.decode('utf-8')]* word_tfidf_val
    print all_id[sub],
    for x in list(numpy.array(doc_val).reshape(-1,)):
        print x,
    print


word2vec_file = sys.argv[1]
doc_file = sys.argv[2]
output_file = sys.argv[3]

f = open(word2vec_file, 'r')
line = f.readline()
line = line.strip('\n')
line_val = line.split(' ')
term_num = int(line_val[0])
feature_size = int(line_val[1])

counter = defaultdict(int)
word2vec = defaultdict(np.matlib.matrix)
while 1:
    line = f.readline()
    if not line:
        break
    line = line.strip('\n')
    if not line:
        continue
    line_val = line.split(' ')
    vector = map(float,line_val[1:feature_size+1])
    term = line_val[0]
    counter[term if isinstance(term, unicode) else unicode(term, 'utf-8')] += 1
    word2vec[term if isinstance(term, unicode) else unicode(term, 'utf-8')] = mat(vector)

print 'Finish making dic'
corpus = []
all_id = []

dfs = {}

f = open(doc_file, 'r')
while 1:
    line = f.readline()
    if not line:
        break
    line=line.strip('\n')
    if not line:
        continue
    word_list = line.split(' ')
    all_id.append(word_list[0])
    one_doc = {}
    for w in word_list[1:]:
        if w not in one_doc:
            one_doc[w] = 1
            if w not in dfs:
                dfs[w] = 1
            else:
                dfs[w] += 1
        else:
            one_doc[w] += 1
            dfs[w] += 1
    corpus.append(one_doc)

print 'Finish making corpus'

doc_num = len(corpus)

idfs = precompute_idfs(df2idf, dfs, doc_num)
print 'Finish calculating idfs'

print 'doc size: ', doc_num, 'term_size: ', term_num

f=open(output_file,'w')
old=sys.stdout
sys.stdout=f
for i in xrange(len(corpus)):
    doc = corpus[i]
    vector = [(term, tf * idfs.get(term)) for term, tf in doc.items() if idfs.get(term, 0.0) != 0.0]
    vector = unitvec(vector)
    # print 'Finish calculating tfidf'
    print_title_vec(i, vector)
    # print 'Finish doc ', i

sys.stdout=old
f.close()