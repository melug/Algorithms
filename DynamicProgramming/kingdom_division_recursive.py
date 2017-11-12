import unittest

class TestCountDivision(unittest.TestCase):

    def test1(self):
        c = [
            [ 0, 1 ],
            [ 0, 2 ],
        ]
        t = self.buildTree(c, 3)
        self.assertEqual(2, 2*count_division(0, t)[0])

    def buildTree(self, connections, size):
        tree = [ [] for i in xrange(size) ]
        for u, v in connections:
            tree[u].append(v)
            tree[v].append(u)
        return tree


def count_division(start, tree):
    if len(tree[start])==0:
        return (0, 1)
    current_valid, current_invalid = 1, 1
    for child in tree[start]:
        tree[child].remove(start)
        valid_child, invalid_child = count_division(child, tree)
        current_invalid *= valid_child
        current_valid *= (2*valid_child+invalid_child)
    current_valid -= current_invalid
    return (current_valid, current_invalid)


if __name__=='__main__':
    n = input()
    tree = [[] for i in xrange(n) ]
    for i in xrange(n-1):
        u, v = map(int, raw_input().split(' '))
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    print((2*count_division(0, tree)[0]) % (10**9+7))
