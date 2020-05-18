import random
import os, sys

words_per_day=20
file=open("data.txt","r")
l=file.readlines()
n=len(l)
random.shuffle(l)
cur=[]
cur_test=[]
for i in range (0,n):
    cur.append(l[i])
    cur_test.append(l[i].split(' ',1))
    if (i+1)%words_per_day==0:
        path="./%d"%(int(i/words_per_day)+1)
        if not os.path.isdir(path):
            os.mkdir( path )
        f=open(path+"/words.txt",'w')
        f_t=open(path+"/tests.txt",'w')
        f.write("day %d:\n\n"%(int(i/words_per_day)+1))
        f_t.write("day %d:\n\n"%(int(i/words_per_day)+1))
        for j in cur:
            f.write(j)
        for j in cur_test:
            f_t.write(j[0]+"\n")
        f.close()
        f_t.close()
        cur=[]
        cur_test=[]
