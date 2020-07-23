# Given array of strings "productName, PopularityScoreAsaStringOutOf100, and priceIntegerAsaString"
# how would you rank the items by popularity. If there is a tie with pop score, place the cheaper priced item first.  
import functools
if __name__ == '__main__':
    def comp(x1, x2):
        if x1[1] < x2[1]:
            return 1
        elif x1[1] == x2[1]:
            if x1[2] < x2[2]:
                return -1
            else:
                return 1
        else:
            return -1

    x = [('a', 10, 10), ('b', 9, 9), ('k', 10, -1), ('c', 10, 5), ('d', 11, 2), ('e', 10, 0), ('j', 10, -10)]
    s = sorted(x, key= functools.cmp_to_key(comp))
    assert s == [('d', 11, 2) , ('j', 10, -10) ,  ('k', 10, -1), ('e', 10, 0), ('c', 10, 5), ('a', 10, 10), ('b', 9, 9)]