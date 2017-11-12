import unittest

class Test1(unittest.TestCase):

    def setUp(self):
        self.roads = [
            [1, 2],
            [1, 3],
            [3, 4],
            [3, 5],
        ]
        self.n = 5

    def test_algo(self):
        roads = build_tree(self.roads, self.n)
        self.assertEqual(roads, [[], [2, 3], [1], [1,4,5], [3], [3]])
        cleaned_trees = clean_tree(roads, 1)
        self.assertEqual(cleaned_trees, [[], [2, 3], [], [4,5], [], []])
        combinations_0 = dfs(cleaned_trees, 1, 0)
        self.assertEqual(combinations_0, 2)

def print_trace(func):
    def log(*args, **kwargs):
        result = func(*args, **kwargs)
        print(args[1:], 'result=', result)
        return result
    return log

def build_tree(roads, n):
    child_tree = [[] for i in xrange(n+1)]
    for s, e in roads:
        child_tree[s].append(e)
        child_tree[e].append(s)
    return child_tree

def clean_tree(roads, start):
    nodes = [start]
    while len(nodes)!=0:
        s = nodes.pop(0)
        for child in roads[s]:
            roads[child].remove(s)
            nodes.append(child)
    return roads

def opposite_color(color):
    return 1 if color==0 else 0

@print_trace
def dfs(roads, start, color, length):
    '''return (valid, invalid) tuple'''
    opposite = opposite_color(color)
    vo = 1
    v = 1
    for node in roads[start]:
        if len(roads[node])!=0:
            valid_same_color, invalid_same_color = dfs(roads, node, color)
            valid_opposite_color, invalid_opposite_color = dfs(roads, node, opposite)
        v_c, i_c = dfs(roads, node, color, 1)
        v_o, i_o = dfs(roads, node, opposite, 2)
        vo *= v_o
        v *= (v_o+v_c)
    # valid combinations
    v -= vo
    # invalid combinations
    return (v, vo)

if __name__=='__main__':
    n = input()
    roads = []
    for i in xrange(n):
        roads.append(map(int, raw_input().split(' ')))
    print(dfs(roads, 1, 0)+dfs(roads, 1, 1))

