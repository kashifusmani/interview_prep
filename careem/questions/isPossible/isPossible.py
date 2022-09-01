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


def is_p(a,b,c,d):
    if a == c and b == d:
        return True
    if a > c or b > d:
        return False
    else:
        return is_p(a+b, b, c,d) or is_p(a, b+a, c,d)

if __name__ == '__main__':
    print(is_p(1,4,5,9))

    print(is_p(1,1,5,2))

    print(is_p(1,2,3,6))