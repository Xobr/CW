class apriori_modify:

    path = None
    minSupport = 0.2

    def __init__(self,pt):
        self.path = pt

    def one_check(self, line, elements):
        for j in elements:
            if not (line[j] == 1):
                return 0
        return 1

    def parse_line(self,line):
        return [int(i) for i in line.split(',')]

    def supportMining(self,res1):
        res = list()
        for line in res1:
            rs = self.supportOneRes1(line)
            if not(rs==None):
                res.append(rs)
        return res

    def supportOneRes1(self,res1):
        ln = len(res1[0])
        if(ln==1):
            return None
        el = list(res1[0])
        el.remove(res1[0][ln-1])
        supp = self.get_Support(res1[0][ln-1],el)
        if(supp<self.minSupport):
            return None
        res = list()
        el.append(res1[0][ln-1])
        res.append([el])
        res.append(res1[1])
        res.append(supp)
        return res


    def get_Support(self,mainElement,elements):
        mainSum = 0
        sum = 0
        for line in open(self.path):
            pline =self.parse_line(line)
            elS = self.one_check(pline,elements)
            if not(elS == 1):#not(pline[mainElement]==1):
                continue
            sum = sum + elS
            if (pline[mainElement]==1):
                mainSum = mainSum + 1
        return float(mainSum)/float(sum)

    def get_P(self, elements):
        sum = 0
        for line in open(self.path):
            pline =self.parse_line(line)
            sum = sum + self.one_check(pline, elements)
        return sum

    def get_start_set(self,dataset,minsupp):
        return len(dataset[0])

    def getSizeOfDataset(self,dataset):
        res = 0
        for line in open(self.path):
            res = res + 1
        return  res

    def aprori(self,dataset, min_support_percent):
        min_support = min_support_percent * self.getSizeOfDataset(dataset)
        ss = self.get_start_set(dataset,min_support)
        start_list = list()
        result = list()
        for elem in ss:
            supp = self.get_P([elem])
            if supp >= min_support:
                start_list.append([elem])
                result.append([[elem], supp])
        next_list = list(start_list)
        while (len(next_list) > 0):
            lastLs = list(next_list)
            next_list = list()
            for elem in lastLs:
                #return result
                for st in start_list:
                    if not (st[0] in elem):
                        crr = list(elem)
                        crr.append(st[0])
                        supp = self.get_P(crr)
                        if supp >= min_support:
                            next_list.append(crr)
                            result.append([crr, supp])
            break
        return result

    def get_product_dict(self,cstr):
        res = dict()
        for line in open(cstr):
        #with open(cstr) as f:
           # line = f.readline()
            lsss = list(line)

            ls = line.split(';')
            #if len(ls) < 2:
            #    continue
            #print len(ls[0])
            key = int(ls[0])
            res[key] = ls[1]
        return res

