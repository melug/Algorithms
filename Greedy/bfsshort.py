
class qnode:

    def __init__(self, data, nnode):
        self.data = data
        self.next = nnode

class queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, n):
        if self.head is None:
            self.head = qnode(n)
            self.tail = self.head
        else:
            c = qnode(n)
            self.tail.next = c
            self.tail = c

    def pop(self):
        h = self.head
        self.head = self.head.tail
        return h

    def is_empty(self):
        return self.head is None


def shortest_path(n, m, r, s):
    '''
    n - nodes
    m - edges
    r - relations r[i]=[j] is i-th node connected j-th
    s - start node
    '''
    marked = []


if __name__=='__main__':
    q = input()
        n, m = map(int, raw_input().split(' '))
        r = [ [] for i in xrange(n) ]
        for i in xrange(len(m)):
            u, v = map(int, raw_input().split(' '))
            r[u-1].append(v-1)
        s = input()

