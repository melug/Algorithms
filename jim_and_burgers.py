
if __name__=='__main__':
    n = int(raw_input())
    orders = []
    for i in range(1, n+1):
        t, d = map(int, raw_input().split(' '))
        orders.append([ t+d, i ])
    orders.sort()
    orders = map(lambda order:order[1], orders)
    print(' '.join(map(str, orders)))
