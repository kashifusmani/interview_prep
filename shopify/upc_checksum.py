# Write a function to validate the checksum in a UPC code. 
# https://gist.github.com/corpit/8204593

def add_check_digit(upc_str):
    """
    Returns a 12 digit upc-a string from an 11-digit upc-a string by adding
    a check digit
    >>> add_check_digit('02345600007')
    '023456000073'
    >>> add_check_digit('21234567899')
    '212345678992'
    >>> add_check_digit('04210000526')
    '042100005264'
    """

    upc_str = str(upc_str)
    if len(upc_str) != 11:
        raise Exception("Invalid length")

    odd_sum = 0
    even_sum = 0
    for i, char in enumerate(upc_str):
        j = i+1
        if j % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)

    total_sum = (odd_sum * 3) + even_sum
    mod = total_sum % 10
    check_digit = 10 - mod
    if check_digit == 10:
        check_digit = 0
    return upc_str + str(check_digit)


def validate_check_digit(upc_str):
    upc = str(upc_str)[0:11]

    odd_sum = 0
    even_sum = 0
    for i, char in enumerate(upc):
        j = i+1
        if j % 2 == 0:
            even_sum += int(char)
        else:
            odd_sum += int(char)

    total_sum = (odd_sum * 3) + even_sum
    mod = total_sum % 10
    check_digit = 10 - mod
    if check_digit == 10:
        check_digit = 0
    return check_digit == int(upc_str[11])

if __name__ == '__main__':
    assert validate_check_digit('023456000073') == True
    assert validate_check_digit('023456000072') == False
    assert validate_check_digit('212345678992') == True
    assert validate_check_digit('212345678994') == False
    assert validate_check_digit('042100005264') == True
    assert validate_check_digit('042100005265') == False