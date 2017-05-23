import pandas as pd
import numpy as np

def one_check(dataset,i,elements):
    for j in elements:
        if not (dataset[i][j] == 1):
            return 0
    return 1

def get_support(dataSet, elements):
    sum = 0
    for i in range(0,len(dataSet)):
        sum = sum + one_check(dataSet,i,elements)
    return sum

def aprori(dataset,min_support):
    ln = len(dataset[0])
    start_list = list()
    result = list()
    for elem in range(0,ln):
        supp = get_support(dataset,[elem])
        if supp >= min_support:
            start_list.append([elem])
            result.append([[elem],supp])
    next_list = list(start_list)
    while(len(next_list)>0):
        lastLs = list(next_list)
        next_list = list()
        for elem in lastLs:
            for st in start_list:
                if not(st[0] in elem):
                    crr = list(elem)
                    crr.append(st[0])
                    supp = get_support(dataset,crr)
                    if supp >= min_support:
                        next_list.append(crr)
                        result.append([crr,supp])
        break
    return result

def get_product_dict(cstr):
    res = dict()
    for line in open(cstr):
        ls = line.split(';')
        if len(ls) < 2:
            continue
        res[int(ls[0])] = ls[1]
    return res


dc = get_product_dict('products.csv')
print 'read Products'
ls = list()
for line in open('resAp.csv'):
    la = line.split(',')
    ls.append([int(i) for i in la])
print 'Create tabls'
#table = pd.read_csv('resAp_1.csv')

print 'Start algo'
#print 'readed'
#arr = np.asarray(table)
res = aprori(ls,200)
for elem in res:
    for pr in elem[0]:
        print dc[pr]
    print elem[1]
    print '___'