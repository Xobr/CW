import datetime
from apriori_dict import apriori_dict

def print_time():
    print datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")


print_time()
print 'start'
ap = apriori_dict('table.txt','products.txt')
ap.minSupport = 0.2
ap.read()
print_time()
print 'strart app'
print_time()
res1 = ap.aprori(ap.dataset,2)
res = ap.supportMining(res1)
print print_time()
print 'finish'
print_time()
for el in res:
    print el
ap.print_res(res)


