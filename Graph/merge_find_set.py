
def find(mfs, e):
    '''
    return the connected component of e
    '''
    t = e
    p = []
    while mfs[t]!=t:
        t = mfs[t]
        p.append(t)
    for i in p:
        mfs[i] = t
    return t

def merge(mfs, e0, e1):
    '''
    merge the cc of e0, e1
    '''
    p0 = find(mfs, e0)
    p1 = find(mfs, e1)
    mfs[p1] = p0

def initialize(n):
    '''
    initialize mfs
    '''
    return range(n)

