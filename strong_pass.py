
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

def contains(s0, s1):
    for s in s0:
        if s in s1:
            return True
    return False

if __name__=='__main__':
    n = input()
    s = raw_input()
    r = 0
    if not contains(numbers, s):
        r += 1
    if not contains(lower_case, s):
        r += 1
    if not contains(upper_case, s):
        r += 1
    if not contains(special_characters, s):
        r += 1
    if len(s)+r>=6:
        print(r)
    else:
        print(6-len(s))


