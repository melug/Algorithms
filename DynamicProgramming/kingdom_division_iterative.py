import copy
import unittest

class TestCountDivision(unittest.TestCase):

    def test1(self):
        c = [
            [ 0, 1 ],
            [ 0, 2 ],
        ]
        t = self.buildTree(c, 3)
        self.assertEqual(2, count_division(0, t))

    def buildTree(self, connections, size):
        tree = [ [] for i in xrange(size) ]
        for u, v in connections:
            tree[u].append(v)
            tree[v].append(u)
        return tree

def clean_parent_tree(tree, parent):
    nodes = [ parent ]
    while len(nodes)!=0:
        node = nodes.pop(0)
        for child in tree[node]:
            tree[child].remove(node)
            nodes.append(child)


def count_division(start, tree):
    parent_tree = copy.deepcopy(tree)
    clean_parent_tree(parent_tree, 0)
    leaves = [ i for i, node in enumerate(parent_tree) if len(node)==0 ]
    valid = [0]*len(tree)
    invalid = [0]*len(tree)
    while len(leaves)!=0:
        node = leaves.pop()
        if len(parent_tree[node])==0:
            valid[node] = 0
            invalid[node] = 1
        else:
            current_valid, current_invalid = 1, 1
            for child in parent_tree[node]:
                current_invalid *= valid[child]
                current_valid *= (2*valid[child]+invalid[child])
            current_valid -= current_invalid
            valid[node] = current_valid
            invalid[node] = current_invalid
        if len(tree[node])!=0:
            parent = tree[node].pop() # delete only connection
            tree[parent].remove(node)
            if start==parent and len(tree[parent])==0:
                leaves.append(parent)
            elif start!=parent and len(tree[parent])==1:
                leaves.append(parent)
    return valid[0]*2


if __name__=='__main__':
    n = input()
    tree = [[] for i in xrange(n) ]
    for i in xrange(n-1):
        u, v = map(int, raw_input().split(' '))
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    print(count_division(0, tree) % (10**9+7))
