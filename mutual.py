

if __name__=='__main__':
    t = input()
    for i in xrange(t):
        a, b, x = map(int, raw_input().split(' '))
        c = b
        numbers = []
        while c>=a:
            divides = False
            for i in xrange(c+1, b+1):
                if i%c==0:
                    divides = True
                    break
            if not divides:
                numbers.append(c)
                x -= 1
                if x==0:
                    break
            c -= 1
        if x==0:
            print(' '.join(map(str, numbers)))
        else:
            print(-1)


