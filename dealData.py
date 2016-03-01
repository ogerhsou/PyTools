__author__ = 'oger'
import jieba, os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

walk = os.walk('test')
for root, dirs, files in walk:
    for name in files:
        f = open(os.path.join(root, name), 'r')
        while 1:
            line = f.readline()
            line = f.readline()
            if not line:
                break;
            wordList = line.split(',')
            for word in wordList:
                print word,
