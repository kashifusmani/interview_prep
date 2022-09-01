def permute(s):
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(0, len(s)):
        for entry in permute(s[:i] + s[i+1:]):
            result.append(s[i] + entry)
    return result


def permute_with_conditions(s):
    if len(s) <= 1:
        return {s[0][0] + s[0][1]}
    result = set()
    for i in range(0, len(s)):
        curr_elem = s[i]
        rest = s[:i] + s[i+1:]
        for entry in permute_with_conditions(rest):
            cur_priority = curr_elem[0]
            cur_delivery = curr_elem[1]
            elems = []
            k = 0
            while k < len(entry):
                elems.append(entry[k] + entry[k+1])
                k += 2

            for j in range(0, len(elems)):
                result.add(str(''.join(elems[:j])) + cur_priority + str(''.join(elems[j:])) + cur_delivery)
                result.add(str(''.join(elems[:j])) + cur_priority + cur_delivery +  str(''.join(elems[j:])) )
                result.add(cur_priority + str(''.join(elems[:j])) + cur_delivery +  str(''.join(elems[j:])) )

    return result

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def countOrders(n):
    combs = 1
    i = (n*2) - 1
    while i > 0:
        combs = combs * i
        i = i - 2
    return combs * factorial(n)

if __name__ == '__main__':
    print(permute('abc'))
    #print(is_perm('AB', 'BAC'))
    #print(len(permute_with_conditions([('P1', 'D1'), ('P2', 'D2'), ('P3', 'D3')])))
    #print(countOrders(8))
