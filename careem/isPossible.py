def isPossible(a, b, c, d):
    if a == c and b == d:
        return "Yes"
    if a > c or b > d:
        return "No"
    if max(c, d) == d:
        d = d - c
    else:
        c = c - d
    return isPossible(a,b,c,d)
