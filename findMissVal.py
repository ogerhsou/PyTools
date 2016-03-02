__author__ = 'oger'

import sys

from gensim import corpora, models
reload(sys)
sys.setdefaultencoding('utf-8')

dic = corpora.Dictionary.load('dic.dat')

miss_val = 0
f = open('vectors.txt', 'r')
while 1:
    line = f.readline()
    if not line:
        break
    line = line.strip('\n')
    if not line:
        continue
    word = line if isinstance(line, unicode) else unicode(line, 'utf-8')
    # word = line.decode('utf-8')
    if word not in dic.token2id:
        miss_val += 1
        print word

print miss_val


