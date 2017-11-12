#!/bin/python

def abs(n):
    return n if n>0 else -n

def min_diff(a):
    a.sort()
    diff = abs(a[1]-a[0])
    for i in xrange(2, len(a)):
        diff = min(diff, abs(a[i]-a[i-1]))
    return diff

if __name__=='__main__':
    n = input()
    a = map(int, raw_input().split(' '))
    print(min_diff(a))
