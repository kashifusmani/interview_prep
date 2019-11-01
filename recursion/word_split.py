'''
Create a function which takes in a String phrase and list_of_words.
The function will determine if it is possible to split the string in a way in which words can be made from the list.
You can assume the phrase will only contain words found in the dictionary if it is completely splittable
word_split('themanran', ['the','ran','man']) => ['the', 'man', 'ran']
word_split('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']) => ['i', 'love', 'dogs', 'John']
word_split('themanran', ['clown','ran','man'])
'''

def word_split(phrase, list_of_words, output=[]):
    # This solution will not print the result in order
    if len(phrase) == 0:
        return output
    elif len(phrase) > 0 and list_of_words == []:
        return []
    else:
        first_item = list_of_words[0]
        list_of_words.remove(first_item)
        if first_item in phrase:
            output.append(first_item)
            return word_split(phrase.replace(first_item, ''), list_of_words, output)
        else:
            return word_split(phrase, list_of_words, output)

def word_split_2(phrase, list_of_words, output = None):
    #Better than above since it does not perform the hacky replace() on the string - which can be a problem if we have "love" and "loves".
    #Complexity is O(mn) where n is length of list and m is number of tokens in the string.
    if output is None: #If we default output=[], it would be overwritten for every recursion!
        output = []

    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split_2(phrase[len(word):], list_of_words, output)
    return output

if __name__ == '__main__':
    #print(word_split('themanran', ['the','ran','man']))
    #print(word_split_2('ilovedogsJohn', ['i', 'am', 'a', 'dogs', 'lover', 'love', 'John']))
    print (word_split_2('themanran', ['the','ran','man']))