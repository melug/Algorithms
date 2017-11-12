
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

def no_pairs(N, P, pairs):
    msf = initialize(N)
    for pair in pairs:
        merge(msf, pair[0], pair[1])
    c_sizes = [0]*N
    for astronaut in xrange(N):
        c_sizes[find(msf, astronaut)] += 1
    S = N
    R = 0
    for i in xrange(N):
        S -= c_sizes[i]
        R += c_sizes[i]*S
    return R

if __name__=='__main__':
    N, P = map(int, raw_input().split(' '))
    pairs = []
    for i in xrange(P):
        pairs.append(map(int, raw_input().split(' ')))
    print(no_pairs(N, P, pairs))
