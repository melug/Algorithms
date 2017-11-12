

def abc(a, b, c, d):
    if any(map(lambda x: x<0, [ a, b, c, d ])):
        return 0
    if a==b==c==d:
        return 2
    if a==c and b==d:
        return 1
    return 0

print(abc(1, 1, 1, 1))
print(abc(-1, 1, 1, 1))
print(abc(2, 1, 2, 1))
print(abc(1, 2, 3, 4))
