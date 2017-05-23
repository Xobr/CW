class apriori_modify:

    path = None

    def __init__(self,pt):
        self.path = pt

    def one_check(self, line, elements):
        for j in elements:
            if not (line[j] == 1):
                return 0
        return 1

    def parse_line(self,line):
        return [int(i) for i in line.split(',')]

    def get_support(self, elements):
        sum = 0
        for line in open(self.path):
            pline =self.parse_line(line)
            sum = sum + self.one_check(pline, elements)
        return sum

    def get_start_set(self,dataset):
        return len(dataset[0])

    def aprori(self,dataset, min_support):
        ss = self.get_start_set(dataset)
        start_list = list()
        result = list()
        for elem in ss:
            supp = self.get_support([elem])
            if supp >= min_support:
                start_list.append([elem])
                result.append([[elem], supp])
        next_list = list(start_list)
        while (len(next_list) > 0):
            lastLs = list(next_list)
            next_list = list()
            for elem in lastLs:
                for st in start_list:
                    if not (st[0] in elem):
                        crr = list(elem)
                        crr.append(st[0])
                        supp = self.get_support(crr)
                        if supp >= min_support:
                            next_list.append(crr)
                            result.append([crr, supp])
            break
        return result

    def get_product_dict(self,cstr):
        res = dict()
        for line in open(cstr):
            ls = line.split(';')
            if len(ls) < 2:
                continue
            key = int(ls[0])
            res[key] = ls[1]
        return res

