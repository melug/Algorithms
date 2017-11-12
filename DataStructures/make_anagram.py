
def abs(x):
    return x if x>=0 else -x

def make_anagram(a, b):
    a_freq = [0]*26
    b_freq = [0]*26
    for c in a:
        a_freq[ord(c)-ord('a')] += 1
    for c in b:
        b_freq[ord(c)-ord('a')] += 1
    return sum(abs(x-y) for x, y in zip(a_freq, b_freq))

if __name__=='__main__':
    a = raw_input()
    b = raw_input()
    print(make_anagram(a, b))
