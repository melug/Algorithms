import unittest

class Test(unittest.TestCase):

    def test_min_candes(self):
        '''
        scores = [1, 5, 6, 4, 3, 2, 1]
        print('scores', scores)
        print('candies', min_candies(scores))
        scores = [5, 5, 5, 4, 4, 2, 1, 2, 2, 3, 3, 3, 4]
        print('scores', scores)
        print('candies', min_candies(scores))
        '''
        scores = [1, 4, 3, 2, 1, 9]
        print('scores', scores)
        print('candies', min_candies(scores))

def min_candies(scores):
    total_candies = 1
    last_candy = 1
    last_peak = -1
    increasing_length = 0
    #print(0, '.', last_candy)
    for i in xrange(1, len(scores)):
        if scores[i]>scores[i-1]:
            last_candy += 1
            last_peak = -1
            increasing_length = 0
            total_candies += last_candy
            #print(i, '.', last_candy)
        elif scores[i]<scores[i-1]:
            if last_peak==-1:
                last_peak = last_candy
            last_candy = 1
            increasing_length += 1
            #print('last_candy', last_candy)
            #print('last_peak', last_peak)
            #print('increasing_length', increasing_length)
            if increasing_length<last_peak:
                total_candies += increasing_length
                #print('did not reach the peak')
                #print(i, '. add 1 to last', increasing_length, 'candies')
            else:
                last_peak += 1
                total_candies += (increasing_length+1)
                #print(i, '. add 1 to last', increasing_length+1, 'candies')
            #print(i, '.', last_candy)
        else:
            last_candy = 1
            last_peak = -1
            increasing_length = 0
            total_candies += last_candy
            #print(i, '.', last_candy)
    return total_candies

if __name__=='__main__':
    N = input()
    scores = []
    for i in xrange(N):
        scores.append(input())
    print(min_candies(scores))
