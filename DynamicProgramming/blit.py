
def blit(A, x, y, N):
    if N==1:
        return
    for x in xrange(N/2):
        for y in xrange(N/2):
            A[y][x], A[y][x+N], A[y+N][x+N], A[y+N][x] = \
                A[y+N][x], A[y][x], A[y][x+N], A[y+N][x+N]
    return A

if __name__=='__main__':
    pass
