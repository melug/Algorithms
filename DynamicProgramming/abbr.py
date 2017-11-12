import unittest

class Test(unittest.TestCase):

    def testMatch(self):
        #self.assertEqual(False, is_it_possible_to_match('monGolia', 'NO'))
        self.assertEqual(True, is_it_possible_to_match('daBcd', 'ABC'))

def imatch(x, y):
    return x.lower()==y.lower()

def convert(value):
    return '1' if value else '0'

def print_table(table):
    for row in table:
        print(' '.join(map(convert, row)))

def is_it_possible_to_match(a, b):
    table = [[False for i in xrange(len(a))] for j in xrange(len(b))]
    table[0][0] = imatch(a[0], b[0])
    for j in xrange(1, len(table[0])):
        if imatch(a[j], b[0]):
            table[0][j] = True
        else:
            if a[j].isupper():
                table[0][j] = False
            else:
                table[0][j] = table[0][j-1]
    for i in xrange(1, len(table)):
        table[i][0] = False
    for j in xrange(1, len(b)):
        for i in xrange(1, len(a)):
            if imatch(a[i], b[j]):
                if a[i].isupper():
                    table[j][i] = table[j-1][i-1]
                else:
                    table[j][i] = table[j-1][i-1] or table[j][i-1]
            else:
                if a[i].isupper():
                    table[j][i] = False
                else:
                    table[j][i] = table[j][i-1]
    return table[len(b)-1][len(a)-1]

if __name__=='__main__':
    q = input()
    for i in xrange(q):
        a = raw_input()
        b = raw_input()
        result = is_it_possible_to_match(a, b)
        if result:
            print('YES')
        else:
            print('NO')
