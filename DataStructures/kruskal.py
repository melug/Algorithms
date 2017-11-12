import heapq

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

def mst(n, m, edges):
    heapq.heapify(edges)
    mfs = initialize(n)
    cc = n # number of disjoint set
    mst_weight = 0
    while cc>1:
        w, a, b = heapq.heappop(edges)
        cc_of_a, cc_of_b = find(mfs, a), find(mfs, b)
        if cc_of_a!=cc_of_b:
            mst_weight += w
            merge(mfs, cc_of_a, cc_of_b)
            cc -= 1
    return mst_weight

if __name__=='__main__':
    n, m = map(int, raw_input().split(' '))
    edges = []
    for i in xrange(m):
        a, b, w = map(int, raw_input().split(' '))
        edges.append([w, a-1, b-1])
    print(mst(n, m, edges))

