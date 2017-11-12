


def min_cost(n, m, clib, croad, roads):
    cities = [0]*n
    total_cost = 0
    for index, marked in enumerate(cities):
        if marked==0:
            cities_to_mark = [ index ]
            number_of_cities_marked = 0
            while len(cities_to_mark)!=0:
                next_cities_to_mark = []
                for city in cities_to_mark:
                    if cities[city]==0:
                        cities[city] = 1
                        number_of_cities_marked += 1
                    for next_city in roads[city]:
                        if cities[next_city]==0:
                            next_cities_to_mark.append(next_city)
                cities_to_mark = next_cities_to_mark
            total_cost += min(number_of_cities_marked*clib,
                    (number_of_cities_marked-1)*croad+clib)
    return total_cost


if __name__=='__main__':
    q = int(input())
    for i in range(q):
        n, m, clib, croad = map(int, input().split(' '))
        roads = [[] for j in range(n)]
        for j in range(m):
            u, v = map(int, input().split(' '))
            roads[u-1].append(v-1)
            roads[v-1].append(u-1)
        print(min_cost(n, m, clib, croad, roads))

