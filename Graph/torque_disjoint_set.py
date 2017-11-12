

def find(mfs, e):
    t = e
    p = []
    while mfs[t]!=t:
        t = mfs[t]
        p.append(t)
    for i in p:
        mfs[i] = t
    return t

def merge(mfs, e0, e1):
    p0 = find(mfs, e0)
    p1 = find(mfs, e1)
    mfs[p1] = p0

def initialize(n):
    return range(n)

def min_cost(n, m, clib, croad, roads):
    total_cost = 0
    mfs = initialize(n)
    for road in roads:
        merge(mfs, road[0]-1, road[1]-1)
    component_sizes = [0]*n
    for city in xrange(n):
        component_sizes[find(mfs, city)] += 1
    for csize in component_sizes:
        if csize!=0:
            total_cost += min(csize*clib,
                    (csize-1)*croad+clib)
    return total_cost


if __name__=='__main__':
    q = int(raw_input())
    for i in range(q):
        n, m, clib, croad = map(int, raw_input().split(' '))
        roads = []
        for j in range(m):
            roads.append(map(int, raw_input().split(' ')))
        print(min_cost(n, m, clib, croad, roads))

