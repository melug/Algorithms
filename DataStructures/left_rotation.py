
def rotate(n, d, a):
    d %= n
    for i in xrange(d, n):
        yield a[i]
    for j in xrange(0, d):
        yield a[j]

if __name__=='__main__':
    n, d = map(int, raw_input().split(' '))
    a = map(int, raw_input().split(' '))
    print(' '.join(map(str, rotate(n, d, a))))
