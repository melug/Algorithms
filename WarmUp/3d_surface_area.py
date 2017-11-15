
def surface_area(H, W, A):
    S = 0
    for i in xrange(1, H+1):
        for j in xrange(1, W+1):
            S += max(0, A[i][j]-A[i-1][j])
            S += max(0, A[i][j]-A[i][j-1])
            S += max(0, A[i][j]-A[i+1][j])
            S += max(0, A[i][j]-A[i][j+1])
    return S+2*H*W

if __name__=='__main__':
    H, W = map(int, raw_input().split(' '))
    A = []
    A.append([0]*(W+2))
    for h in xrange(H):
        A.append([0]+map(int, raw_input().split(' '))+[0])
    A.append([0]*(W+2))
    print(surface_area(H, W, A))

