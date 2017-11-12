

def min_diff(N, K, x):
    x.sort()
    S = temp_S = sum(x[:K])
    min_diff = 0
    for i in xrange(K):
        min_diff += temp_S-x[i]*(K-i)
        temp_S -= x[i]
    prev_diff = min_diff
    for i in xrange(K, N):
        # remove i-K, add i, maintain S and prev_diff
        prev_diff -= S-x[i-K]*K
        prev_diff += (K-1)*x[i]-(S-x[i-K])
        S = S-x[i-K]+x[i]
        min_diff = min(min_diff, prev_diff)
    return min_diff


if __name__=='__main__':
    N = input()
    K = input()
    x = []
    for i in xrange(N):
        x.append(input())
    print(min_diff(N, K, x))
