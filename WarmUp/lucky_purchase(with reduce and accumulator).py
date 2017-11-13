"""
Demonstration of reduce function.
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

def accumulate(best_laptop, laptop):
    if is_lucky(laptop):
        if best_laptop is None:
            return laptop
        elif cmp(best_laptop[1], laptop[1])>0:
            return laptop
    return best_laptop

if __name__=='__main__':
    n = int(raw_input())
    best_laptop = reduce(accumulate, (raw_input().split(' ') for i in xrange(n)), None)
    if best_laptop is None:
        print(-1)
    else:
        print(best_laptop[0])

