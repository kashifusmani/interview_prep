def frequency(s):
    result = {}
    num_count = 1
    i = len(s) - 1
    while(i >= 0):
        if s[i] == ')':
            end = i
            while s[i] != '(':
                i = i -1
            num_count = int(s[i+1:end])
        elif s[i] == '#':
            character_num = int(s[i-2:i])
            if character_num in result:
                result[character_num] = num_count + result[character_num]
            else:
                result[character_num] = num_count
            i = i-2
            num_count = 1
        else:
            character_num = int(s[i])
            if character_num in result:
                result[character_num] = num_count + result[character_num]
            else:
                result[character_num] = num_count
            num_count = 1
        i = i-1
    print(result)
    final_result = []
    for k in range(1, 27):
        if k in result:
            final_result.append(result[k])
        else:
            final_result.append(0)
    print(final_result)
    return final_result


if __name__ == '__main__':
    result = frequency('23#(2)24#25#26#23#(3)')