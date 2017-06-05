from AprioriModify import apriori_modify

class apriori_dict(apriori_modify):
    path = None
    pstr =None
    dataset = None
    prodc_dict = None

    def __init__(self,tstr,pstr):
        self.pstr = pstr
        self.path = tstr

    def is_elements_incheck(self,line,elements):
        for elem in elements:
            if not(elem in line):
                return  False
        return True

    def get_P(self, elements):
        sup = 0
        for elem in self.dataset:
            if(self.is_elements_incheck(elem,elements)):
                sup = sup + 1
        return sup

    def getSizeOfDataset(self, dataset):
        return len(dataset)

    def get_Support(self, mainElement, elements):
        mainSum = 0
        sum = 0
        for line in self.dataset:
            if not(self.is_elements_incheck(line,elements)):
                continue
            sum = sum + 1
            if mainElement in line:
                mainSum = mainSum + 1
        res = float(mainSum)/float(sum)
        return  res


    def get_start_set(self,dataset,min_support):
        self.prodc_dict = self.get_product_dict(self.pstr)
        res = dict()
        for line in dataset:
            for item in line:
                if(item in res.keys()):
                    res[item] = res[item] + 1
                else:
                    res[item] = 1
        resLs = list()
        for it in res.keys():
            if res[it] > min_support:
                resLs.append(it)
        return resLs

    def read(self):
        self.dataset = list()
        for line in open(self.path):
            la = line.split(',')
            self.dataset.append([int(i) for i in la])

    def print_res(self,res):
        for elem in res:
            for st in elem[0][0]:
                print self.prodc_dict[st]
            print elem[1]
            print elem[2]
            print '___'
            print ''



