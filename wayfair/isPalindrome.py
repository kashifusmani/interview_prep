# you can write to stderr for debugging purposes, e.g.
# sys.stderr.write("this is a debug message\n")


def isPalindromeHelper(x):
    if (len(x) == 0 or len(x) == 1):
        return True
    else:
        return x[0].lower() == x[-1].lower() and isPalindromeHelper(x[1:len(x)-1])

def isPalindrome(x):
    if len(x) == 0:
        return False
    else:
        # punctuations = set(['-', ',', ':', '?', '!', ' ', '#'])
        y = ""
        for elem in x:
            if elem.isalpha():
                y += elem
        return isPalindromeHelper(y)

from itertools import combinations

def allPossibleSubstring(x):
    result = [x[a:b] for a, b in combinations(range(len(x)+1), r=2)]
    return result

def getLongestPalindromes(x):
    max_len = -1
    longest_palindromes = []
    for elem in allPossibleSubstring(x):
        if isPalindrome(elem) and len(elem) > max_len:
            max_len = len(elem)

    for elem in allPossibleSubstring(x):
        if isPalindrome(elem) and len(elem) == max_len:
            longest_palindromes.append(elem)
    return longest_palindromes


if __name__ == '__main__':
    assert(isPalindrome("") ==  False)
    assert(isPalindrome("lotion") == False)
    assert(isPalindrome("racecar") == True)
    assert(isPalindrome("Racecar") == True)
    assert(isPalindrome("Step on no pets") == True)
    assert(isPalindrome("No lemon no melons") ==  False)
    assert(isPalindrome("1Eva - can I see bees in a cave?") ==  True)
    assert(isPalindrome("A man, a plan, a canal: Panama!#") == True)

    assert(getLongestPalindromes("Aaaaa") == ["Aaaaa"])
    # assert(getLongestPalindromes("A racecar") == ["racecar"])
    assert(getLongestPalindromes("No lemon no melons") == ["No lemon no melon"])
