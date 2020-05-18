import random
import os, sys

n_new=20
n_old=20
n_hard=10
def getday():
    logfile=open("log.txt",'r')
    line=logfile.readline().split()
    logfile.close()
    return int(line[1])
day=getday()
pool=[]
cur=open("./Words/%d/words.txt"%(day+1),'r')
l=cur.readlines()
poolnew=l[2:].copy()
cur.close()

for i in range (1,day+1):
    cur=open("./Words/%d/words.txt"%i,'r')
    l=cur.readlines()
    pool+=l[2:]
    cur.close()
cur=open("hardwords.txt",'r')
pool2=cur.readlines()
cur.close()
result_old=random.sample(pool,k=n_old)
result_hard=random.sample(pool2,k=min(n_hard,len(pool2)))
l=["new words:\n",'\n']+poolnew+['\n',"old words:\n",'\n']+result_old+result_hard
rd=open("README.md",'w')
for i in l:
    print(i[:-2])
    rd.write(i[:-2]+'\\\n')
