
def swap(s: str, ind1: int, ind2: int):
    if ind1 == ind2:
        return s
    min_ind = min(ind1, ind2)
    max_ind = max(ind1, ind2)
    return s[0:max(0, min_ind)] + s[max_ind] + s[min_ind+1: max_ind] + s[min_ind] + s[min(len(s), max_ind)+1:]

def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    if len(s1) != len(s2):
        return False
    else:
        i = 0
        while i < len(s1):
            try:
                elem_ind = s2.index(s1[i])
            except:
                return False
            if swap(s2, i, elem_ind) == s1:
                return True
            i += 1
        return False

if __name__ == '__main__':
    """
    s = "abcd"
    assert swap(s, 0, 3) == "dbca"
    assert swap(s, 1, 3) == "adcb"
    assert swap(s, 2, 3) == "abdc"
    assert swap(s, 3, 3) == "abcd"

    assert swap(s, 0, 1) == "bacd"
    assert swap(s, 1, 1) == "abcd"
    assert swap(s, 2, 1) == "acbd"
    assert swap(s, 3, 1) == "adcb"

    assert swap(s, 0, 2) == "cbad"
    assert swap(s, 1, 2) == "acbd"
    assert swap(s, 2, 2) == "abcd"
    assert swap(s, 3, 2) == "abdc"

    assert swap(s, 0, 0) == "abcd"
    assert swap(s, 1, 0) == "bacd"
    assert swap(s, 2, 0) == "cbad"
    assert swap(s, 3, 0) == "dbca"
    """

    areAlmostEqual("siyolsdcjthwsiplccjbuceoxmpjgrauocx",
                   "siyolsdcjthwsiplccpbuceoxmjjgrauocx"
                   )
