import unittest

def mergesort(array, start=0, end=None):
    if end is None:
        end = len(array)
    if start==end:
        return array[start]
    mid = (start+end)/2
    array_0 = mergesort(array, start, mid)
    array_1 = mergesort(array, mid+1, end)
    new_array = []
    i0 = 0
    while len(i0)!=len(array_0) or len(i1)!=len(array_1):




