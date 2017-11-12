

def main(array):
    opt = array[0]
    max_opt = opt
    for i in xrange(1, len(array)):
        opt = max(opt+array[i], array[i])
        max_opt = max(max_opt, opt)
    subseq = 0
    if all(map(lambda a:a<0, array)):
        subseq = max(array)
    else:
        subseq = sum(filter(lambda a:a>0, array))
    print('{0} {1}'.format(max_opt, subseq))

if __name__=='__main__':
    T = input()
    for t in xrange(T):
        N = input()
        array = map(int, raw_input().split(' '))
        main(array)
