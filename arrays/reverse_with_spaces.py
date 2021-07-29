def reverse(x):


    space_indices = []

    for i in range(len(x)):
        if x[i] == ' ':
            space_indices.append(i)

    y = list(filter(lambda f: f!= ' ', x))

    start = 0
    end = len(y) - 1

    while(start < end):
        temp = y[start]
        y[start] = y[end]
        y[end] = temp
        start += 1
        end -= 1

    print(y)

    result = []
    for item in y:
        if len(result) not in space_indices:
            result.append(item)
        else:
            result.append(' ')
            result.append(item)
    print(result)




#print(reverse('abc d ef')) # fed c ba
#abc d ef => fbc d ea =>  fed c ba


def rev(x):
    lo = 0
    high = len(x) - 1

    cp = list(x)
    while lo <= high:
        if x[lo] == ' ':
            lo = lo + 1
        if x[high] == ' ':
            high = high - 1
        else :
            temp = cp[lo]
            cp[lo] = cp[high]
            cp[high] = temp
            lo = lo + 1
            high = high - 1
    print(cp)

if __name__ == '__main__':
    rev('abc d ef')