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

    def get_Support(self, mainElement, elements):
        mainSum = 0
        sum = 0
        for elements in self.dataset:
            if(mainElement )

    def get_start_set(self,dataset):
        self.prodc_dict = self.get_product_dict(self.pstr)
        res = list()
        return self.prodc_dict.keys()

    def read(self):
        self.dataset = list()
        for line in open(self.path):
            la = line.split(',')
            self.dataset.append([int(i) for i in la])

    def print_res(self,res):
        for elem in res:
            for st in elem[0]:
                print self.prodc_dict[st]
            print elem[1]
            print '___'
            print ''



