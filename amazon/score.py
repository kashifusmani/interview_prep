

def cal(arr):
    result = []
    i = 0
    while i < len(arr):
        elem = arr[i]
        elem_last_index = arr.rindex(elem)
        unique_chars = list(set(arr[i:elem_last_index]))
        for unique_char in unique_chars:
            last_index_uniq_char = arr.rindex(unique_char)
            if last_index_uniq_char > elem_last_index:
                elem_last_index = last_index_uniq_char
        result.append(len(arr[i: elem_last_index+1]))
        i = elem_last_index+1
    return result


def score(arr):
    result = []

    last_score = 0
    total_score = 0
    for elem in arr:
        if elem == 'X':
            last_score = 2 * last_score
            total_score = total_score + last_score
            result.append((last_score, total_score))
        elif elem == 'Z':
            result.pop()
            last_score, total_score = result[-1]
        elif elem == '+':
            last_score = result[-1][0] + result[-2][0]
            total_score = total_score + last_score
            result.append((last_score, total_score))
        else:
            last_score = elem
            total_score = total_score + last_score
            result.append((last_score, total_score))

    return total_score


if __name__ == '__main__':
    #input = 'ababcbacadefegdehijhklij'
    #print(cal(input))
    #print(cal('abc'))
    #print(cal('abca'))
    input = [5, -2, 4, 'Z', 'X', 9, '+', '+']
    print(score(input))