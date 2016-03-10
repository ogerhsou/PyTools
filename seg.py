#coding:latin1
# from __future__ import print_function
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import jieba
import time
#jieba.enable_parallel(8)   #slower!

string_punc = '\t,\n　. ?;\'[]()`~!@#$%^&*/+_-=<>{}:，。？！·；：‘“【】（）>    、\"\\'.decode('utf-8')
punc_set = set(string_punc)
#print punc_set

def stripPunc(input_text):
    flag = True
    first = True
    lst = jieba.cut(input_text)
    #t1_lst = []
    for token in lst:
        if flag:
            try: 
                int(token)
            except:
                #print 'error id: ', token
                return
            flag = False
            #t1_lst.append(token)
            yield token
        elif token not in punc_set:
            yield token
            #t1_lst.append(token)
    #return t1_lst

cnt = 0
time1 = time.time()
fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')
while 1:
#for line in sys.stdin:
    line = fin.readline()
    if not line:
        break
        #continue
    if len(line) <= 8:
        continue
    else:
        lst = stripPunc(line)
        cnt += 1
        if cnt % 10000 == 0:
            print cnt
            print time.time()-time1
        fout.write((" ".join(lst)+'\n').encode('utf-8'))
