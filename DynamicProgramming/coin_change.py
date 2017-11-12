
def print_opt(opt):
    for r in opt:
        print(r)

def trace(opt, track, x, y, coins):
    if len(track[x][y])==0:
        print([opt[x][y]]+coins)
    else:
        for x0, y0 in track[x][y]:
            trace(opt, track, x0, y0, [opt[x][y]]+coins)

def count_coin_change(n, m, c):
    opt = [ [ 0 for j in xrange(m) ] for i in xrange(n+1) ]
    track = [ [ [] for j in xrange(m) ] for i in xrange(n+1) ]
    for i in xrange(m):
        opt[0][i] = 1
    for i in xrange(1, n+1):
        for j in xrange(m):
            if i>=c[j]:
                opt[i][j] += opt[i-c[j]][j]
                track[i][j].append([i-c[j], j])
            if j>0:
                opt[i][j] += opt[i][j-1]
                track[i][j].append([i, j-1])
    print_opt(opt)
    trace(opt, track, n, m-1, [])
    return opt[n][m-1]

if __name__=='__main__':
    n, m = map(int, raw_input().split(' '))
    c = map(int, raw_input().split(' '))
    print(count_coin_change(n, m, c))
