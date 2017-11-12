import re

def compare_hotel(h0, h1):
    if h0[0]==h1[0]:
        return cmp(h0, h1)
    return -cmp(h0, h1)

def sort_hotels(keywords, hotel_ids, reviews):
    pattern = '|'.join(keywords)
    hotel_and_hits = [0]*max(hotel_ids)
    for hotel_id, review in zip(hotel_ids, reviews):
        hotel_and_hits[hotel_id-1] += len(re.findall(pattern, review, re.I))
    reversed_hotels = [[ hits, hotel_id ] for hotel_id, hits in \
            enumerate(hotel_and_hits)]
    reversed_hotels.sort(cmp=compare_hotel)
    for hit_and_hotel in reversed_hotels:
        print(hit_and_hotel[1]+1)

if __name__=='__main__':
    keywords = raw_input().split(' ')
    n = int(raw_input())
    hotel_ids = []
    for i in xrange(n):
        hotel_ids.append(int(raw_input()))
    reviews = []
    for i in xrange(n):
        reviews.append(raw_input())
    sort_hotels(keywords, hotel_ids, reviews)
