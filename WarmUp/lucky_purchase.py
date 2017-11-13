"""
Demonstration of filter function.
"""

def is_lucky(laptop):
    brand, price = laptop
    fours, sevens = 0, 0
    for c in price:
        if c=='4':
            fours += 1
        elif c=='7':
            sevens += 1
        else:
            return False
    return fours==sevens

def key_laptop(l):
    return l[1]

if __name__=='__main__':
    n = int(raw_input())
    laptops = filter(is_lucky, [ raw_input().split(' ') for i in xrange(n) ])
    if len(laptops)==0:
        print(-1)
    else:
        brand, price = min(laptops, key=key_laptop)
        print(brand)

