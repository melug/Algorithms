
def print_table(table):
    for row in table:
        print(' '.join(map(str, row)))

if __name__=='__main__':
    n, m, k = map(int, raw_input().split(' '))
    table = [[ m for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if i>j:
                table[i][j] = table[i-1][j]-1
            elif i<j:
                table[i][j] = table[i][j-1]-1
            elif i==j==0:
                table[i][j] = m
            else:
                table[i][j] = table[i-1][j-1]+k
    print_table(table)
