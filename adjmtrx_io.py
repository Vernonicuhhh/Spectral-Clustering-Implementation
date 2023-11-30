
def write_adj_mtrx(mtrx,fp):
    with open(fp,'w',encoding = 'utf8') as fout:
        for row in mtrx:
            print(*row, file=fout)

def compat_splitting(line):
    return line.split()

def read_adj_mtrx(fp):
    A = []
    with open(fp,'r',encoding = 'utf8') as fin:
        for _, row in enumerate(fin):
            tab = compat_splitting(row)
            entries =  [float(e) for e in tab]
            A.append(entries)
    return A
