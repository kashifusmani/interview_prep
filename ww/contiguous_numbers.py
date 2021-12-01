def contiguous_number_ranges(numbers):
    result = []
    i = 1
    start_elem = numbers[0]
    while i < len(numbers):
        while i < len(numbers) and ((numbers[i] - numbers[i-1]) == 1 or (numbers[i] - numbers[i-1]) == -1):
            i += 1
        result.append([min(start_elem, numbers[i-1]), max(start_elem, numbers[i-1])])
        if i == len(numbers):
            break
        start_elem = numbers[i]
        if i == len(numbers) - 1:
            result.append([start_elem, start_elem])

        i = i+1
    return result



if __name__ == '__main__':
    print(contiguous_number_ranges([40, 41, 41, 42, 1, 2, 50, 3, 4]))