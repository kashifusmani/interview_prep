"""
you are given a list of sorted words as they would appear in a dictionary, but the language is 'alien' to you.
 Using the words, create a list that shows the order of occurrence of letters in that language's 'alphabet' sequence
Input:  words[] = {"baa", "abcd", "abca", "cab", "cad"}
Output: Order of characters is 'b', 'd', 'a', 'c'
Note that words are sorted and in the given language "baa"
comes before "abcd", therefore 'b' is before 'a' in output.
Similarly we can find other orders.

Input:  words[] = {"caa", "aaa", "aab"}
Output: Order of characters is 'c', 'a', 'b'

# https://www.geeksforgeeks.org/given-sorted-dictionary-find-precedence-characters/
1) Create a graph g with number of vertices equal to the size of alphabet in the given alien language. For example, if the alphabet size is 5, then there can be 5 characters in words. Initially there are no edges in graph.

2) Do following for every pair of adjacent words in given sorted array.
…..a) Let the current pair of words be word1 and word2. One by one compare characters of both words and find the first mismatching characters.
…..b) Create an edge in g from mismatching character of word1 to that of word2.

3) Print topological sorting of the above created graph.

"""


def get_first_non_matching_pair(word1, word2):
    """
    "abc", "bdc" -> (a,b)
    "ab", "abc" -> ('',c)
    "abc", "ab" -> ('c','')
    :return:
    """
    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            return (word1[i], word2[i])

    if len(word1) > len(word2):
        return (word1[len(word2)] , '')
    elif len(word2)> len(word1):
        return ('', word2[len(word1)])


def get_order(words):
    result = []

    prev_word = words[0]
    for i in range(1, len(words)):
        cur_word = words[i]
        result.append(get_first_non_matching_pair(prev_word, cur_word))
        prev_word = cur_word

    prev_tup = result[0]
    final_result = [prev_tup[0]]

    for i in range(1, len(result)):
        cur_tup = result[i]
        if prev_tup[1] == cur_tup[1]:
            final_result.append(cur_tup[0])
        elif prev_tup[1] == cur_tup[0]:
            final_result.append(cur_tup[0])
        else:
            final_result.append(prev_tup[1])
        prev_tup = cur_tup
    return final_result


if __name__ == '__main__':
    print(get_order(["baa", "abcd", "abca", "cab", "cad"]))