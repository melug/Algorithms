import heapq


def is_lower_basket(basket, shop_baskets):
    for basket_at_shop in shop_baskets:
        if basket_at_shop==basket_at_shop|basket:
            return True
    return False

def remove_lower_baskets(basket, shop_baskets):
    index = 0
    while index<len(shop_baskets):
        if basket==basket|shop_baskets[index]:
            # swap with last element
            shop_baskets[index], shop_baskets[-1] =\
                    shop_baskets[-1], shop_baskets[index]
            shop_baskets.pop()
        else:
            index += 1

def min_time(N, M, K, T, roads):
    shop_baskets = [ [] for i in xrange(N) ]
    full_basket = (1<<K)-1
    paths = []
    heapq.heappush(paths, [ 0, 0, 0 ])
    while True:
        current_time, dest, basket = heapq.heappop(paths)
        basket |= T[dest]
        if not is_lower_basket(basket, shop_baskets[dest]):
            remove_lower_baskets(basket, shop_baskets[dest])
            shop_baskets[dest].append(basket)
            if dest==N-1:
                is_complement_covered = is_lower_basket(full_basket-basket, shop_baskets[dest])
                if is_complement_covered:
                    return current_time
            for new_dest, time in roads[dest]:
                heapq.heappush(paths, [ current_time+time, new_dest, basket ])

def main():
    input_stream = raw_input
    N, M, K = map(int, input_stream().split(' '))
    T = [0]*N
    for n in xrange(N):
        for t in map(int, input_stream().split(' '))[1:]:
            T[n] |= 1<<(t-1)
    roads = [[] for i in xrange(N)]
    for m in xrange(M):
        x, y, z = map(int, input_stream().split(' '))
        roads[x-1].append([y-1, z])
        roads[y-1].append([x-1, z])
    print(min_time(N, M, K, T, roads))

if __name__=='__main__':
    main()
