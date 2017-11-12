
def convert_bool(t):
    return 'T' if t else 'F'

def print_table(table):
    for r in table:
        print(' '.join([ convert_bool(c) for c in r ]))

def knapsack(n, a, k):
    table = [ [ False for j in xrange(n+1) ] for i in xrange(k+1) ]
    for i in xrange(n+1):
        table[0][i] = True
    for r in xrange(1, k+1):
        for c in xrange(1, n+1):
            table[r][c] = table[r][c] or table[r][c-1]
            if r-a[c-1]>=0:
                table[r][c] = table[r][c] or table[r-a[c-1]][c-1]
    for i in xrange(k, -1, -1):
        if table[i][n]:
            return i

if __name__=='__main__':
    T = input()
    for t in xrange(T):
        n, k = map(int, raw_input().split(' '))
        a = map(int, raw_input().split(' '))
        print(knapsack(n, a, k))
