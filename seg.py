#coding:latin1
# from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
jieba.enable_parallel(8)

def stripPunc(input_text):
    wordcnt = ""
    flag = True
    first = True
    for token in jieba.cut(input_text):
        if flag:
            print token
            flag = False
        elif token not in " \t,\n.?;'[]()`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“【】（）、\"\\":
            if first:
                wordcnt += token
                first = False
            else:
                wordcnt += ',' + token
    print wordcnt


for line in sys.stdin:
    if not line:
        continue;
    
    if len(line) <= 8:
        continue;
    else:
        stripPunc(line)
        # for w in stripPunc(line):
        # print wordcnt