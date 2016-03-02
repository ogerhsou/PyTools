__author__ = 'oger'

import sys

from gensim import corpora, models
reload(sys)
sys.setdefaultencoding('utf-8')

train_set = []

f = open('pureData.txt', 'r')
while 1:
    line = f.readline()
    if not line:
        break
    line=line.strip('\n')
    if not line:
        continue
    word_list = line.split(' ')
    train_set.append(word_list)

print 'Total Size: ', train_set.__len__()

dic = corpora.Dictionary(train_set)
dic.save('dic.dat')
print 'Finish saving dic'
corpus = [dic.doc2bow(text) for text in train_set]
#should save by serialize
#corpora.MmCorpus.save_corpus('corpus.dat',corpus)
corpora.MmCorpus.serialize('corpus.dat',corpus)
print 'Finish saving corpus'
tfidf = models.TfidfModel(corpus)
tfidf.save('tfidf.dat')
print 'Finish saving tfidf'
corpus_tfidf = tfidf[corpus]
#corpora.MmCorpus.save_corpus('corpus_tfidf.dat',corpus_tfidf)
corpora.MmCorpus.serialize('corpus_tfidf.dat',corpus_tfidf)
print 'Finish saving corpus_tfidf'

# t1 = corpora.Dictionary.load('dic.dat')
# t2 = corpora.MmCorpus('corpus.dat')
# t3 = models.TfidfModel.load('tfidf.dat')
# t4 = corpora.MmCorpus('corpus_tfidf.dat')
