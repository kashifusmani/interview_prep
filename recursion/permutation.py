def permute(s):
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(0, len(s)):
        for entry in permute(s[:i] + s[i+1:]):
            result.append(s[i] + entry)
    return result

def is_perm(a,b):#TODO make it work
    res = 0
    for x,y in zip(a,b):
        res = res ^ int(format(ord(x), 'b')) ^ int(format(ord(y), 'b'))
    return res == 0


if __name__ == '__main__':
    #print(permute('abcd'))
    print(is_perm('AB', 'BAC'))
