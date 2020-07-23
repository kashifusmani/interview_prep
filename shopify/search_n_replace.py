def search(input, word):
    if len(word) > len(input):
        return False
    if input == word:
        return True
    if word == '' and len(input) > 0:
        return True
    cur = word[0]
    for i in range(len(input)):
        if input[i] == cur:
            return search(input[i+1:], word[1:])
    return False


def search_n_replace(input, word, word_2):
    if not search(input, word):
        raise Exception("%s does not exist in %s" % (word, input))

    i = input.index(word)
    result = input[0:i]
    result = result + word_2
    result = result + input[(i+len(word)):]
    return result

# macdonald , do
# macdonald , dos
# macdonald , ma
# macdonald , ld

if __name__ == '__main__':
    assert search('macdonald', 'do') == True
    assert search('macdonald', 'dos') == False
    assert search('macdonald', 'ma') == True
    assert search('macdonald', 'ld') == True
    assert  search_n_replace('macdonalds', 'do', 'dont') == 'macdontnalds'
    assert  search_n_replace('macdonalds', 'donald', '') == 'macs'