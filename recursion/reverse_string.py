def reverse(s):
    if len(s) == 1 or len(s) == 0:
        return s
    return s[len(s)-1] + reverse(s[0: len(s)-1]) # or return reverse(s[1:]) + s[0]

if __name__ == '__main__':
    print(reverse('hello world'))
