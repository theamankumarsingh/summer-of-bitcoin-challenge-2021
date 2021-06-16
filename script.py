import csv
from operator import itemgetter

MAX_WEIGHT = 4000000

def read_mempool(filename='mempool.csv'):
    i=-1
    obj=[]
    file=open(filename)
    objReader=csv.reader(file)
    objReader=list(objReader)
    for r in objReader:
        i+=1        
        if(not(i)):
            continue
        obj.append([i-1]+[r[0]]+[int(r[1])]+[int(r[2])]+[r[3]]+[int(r[1])/int(r[2])]+[True])    
    return obj
def initialize_files(filename_list):
    for n in filename_list:
        file=open(n,'w')
        file.write('')
        file.close()
def write_file(txid,filename='block.txt'):
    file=open(filename,'a')
    file.write(txid+'\n')
    file.close()
def sort_pool(lst,k):
    lst.sort(key = lambda x: (-x[k]))
    return lst

weight=0
fee=0
count=0

initialize_files(['block.txt'])
pool=read_mempool()
fee_rank=sort_pool(pool.copy(),5)
for row in fee_rank:
    s=set(row[4].split(';'))
    parent_set=set()
    for j in range(row[0]):
        if(pool[j][6]):
            parent_set.add(pool[j][1])
    parent_set.add('')
    if(s==(s.intersection(parent_set)) and (weight+row[3])<=MAX_WEIGHT):
        write_file(row[1])
        row[6]=False
        fee+=row[2]
        weight+=row[3]
        count+=1
print(fee,weight,count)