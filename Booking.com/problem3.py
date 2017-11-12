
def delta_encode(array):
    if len(array)==0:
        return
    print(array[0])
    for i in xrange(1, len(array)):
        diff = array[i]-array[i-1]
        if not -127<=diff<=127:
            print(-128)
        print(diff)

delta_encode([11238, 11000, 11009])
