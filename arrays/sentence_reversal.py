def rev_word(s):
    splitted = []

    elem_start = elem_end = 0
    for ind, elem in enumerate(s):
        if elem != ' ' and ind < len(s) -1:
            elem_end = ind
        elif elem != ' ' and ind == len(s) -1:
            splitted.append(s[elem_start: len(s)])
        else:
            if elem_start < elem_end:
                splitted.append(s[elem_start: ind+1].strip())
                elem_start = ind + 1
                elem_end = ind


    start = 0
    end = len(splitted) - 1
    while start < end:
        temp = splitted[start]
        splitted[start] = splitted[end]
        splitted[end] = temp
        start += 1
        end -= 1
    return ' '.join(splitted)


def remove_spaces(s):
    i = 0
    length = len(s)
    words = []
    while i < length:
        if not s[i] == ' ':
            word_start = i
            while i < length and not s[i] == ' ':
                i +=1
            words.append(s[word_start, i])
        i+=1


#Don't do in interview setting
def rev_word_2(s):
    return ' '.join(reversed(s.split()))

#Don't do in interview setting
def rev_words_3(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    word = 'Hi John,    are you ready to go?'
    word_2 = '    space before'
    word_3 = 'space after      '
    word_4 = '   Hello John   how are you     '

    print(rev_word(word))
    print(rev_word(word_2))
    print(rev_word(word_3))
    print(rev_word(word_4))