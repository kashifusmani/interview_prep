def funWithAnagrams(text):
    def _is_anagram(a,b):
        counts = {}
        chars_to_ignore = ['.', ' ']
        for char in chars_to_ignore:
            a = a.replace(char, '')
            b = b.replace(char, '')
        a = a.lower()
        b = b.lower()
        if len(a) != len(b):
            return False
        for char in a:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
        for char in b:
            if char not in counts:
                return False
            else:
                counts[char] -= 1

        for char in counts:
            if counts[char] > 0:
                return False
        return True


    results = [text[0]]
    for word in text[1:]:
        is_anagram = False
        for item in results:
            if _is_anagram(word, item):
                is_anagram = True
        if not is_anagram:
            results.append(word)

    return sorted(results)

if __name__ == '__main__':
    #print(funWithAnagrams( ["code","aaagmnrs","anagrams","doce"]))
    #print(funWithAnagrams(["poke","pkoe","okpe","ekop"]))
    print(funWithAnagrams(["code","doce","ecod","framer", "frame"]))