__author__ = 'oger'

import sys
from gensim import corpora

reload(sys)
sys.setdefaultencoding('utf-8')

dic = corpora.Dictionary.load('dic-all.dat')

f = open('testWord.txt', 'r')
line = f.readline()
while 1:
    line = f.readline()
    if not line:
        break
    line = line.strip('\n')
    if not line:
        continue
    line_val = line.split(' ')

    word_name = line_val[0]
    word = word_name if isinstance(word_name, unicode) else unicode(word_name, 'utf-8')
    # word = line.decode('utf-8')
    # val_list = []
    real_dic = dic.token2id
    if word in real_dic:
        print real_dic[word],
        for i in xrange(1, len(line_val)):
            print line_val[i],
        print
