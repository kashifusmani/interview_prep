
"""
Given two strings S and T, count the number of permutations of S that occur in T

S = "abc" -> abc
T = "cabcbcab"

cab -> abc
abc -> abc
bcb  -> bbc
cbc  -> bcc
bca  -> abc
cab  -> abc

Output = 4 // ["cab", "abc", "bca", "cab"] only the count is required, the actual list of permutations is optional.

bac   acb

{b:1, a: 1, c: 1}


"""


def check_same(a, b):
    res = {}


    for item in b:
        if item not in res:
            return False
        else:
            res[item] = res[item] - 1

    return sum(res.values()) == 0


def calc_perms(s, t):
    if (len(t) < len(s)) or (len(s) == 0) or s is None or t is None:
        return 0

    target_len = len(s)
    result = 0

    counts_s = {}
    for item in s:
        if item not in counts_s:
            counts_s[item] = 1
        else:
            counts_s[item] = counts_s[item] + 1

    counts_perm = {}
    perm = t[0:target_len]
    for item in perm:
        if item not in counts_perm:
            counts_perm[item] = 1
        else:
            counts_perm[item] = counts_perm[item] + 1

    if counts_perm == counts_s:
        result += 1

    last_char = perm[0]
    i = 0
    j = target_len
    while (j < len(t)):

        i += 1
        j += 1
        perm = t[i:j]
        counts_perm[last_char] = counts_perm[last_char] - 1
        new_char = t[j-1]
        if new_char in counts_perm:
          counts_perm[new_char] =   counts_perm[new_char]+1
        else:
            counts_perm[new_char] = 1
        last_char = perm[0]
        if counts_perm == counts_s: # still O(n) but can be improved
            result += 1

    return result


if __name__ == '__main__':
    # "abc", "abc"
    print(calc_perms("abc", "cabcbcab"))
    #print(check_same("bca", "cab"))