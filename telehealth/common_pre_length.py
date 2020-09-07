
def commonPrefix(inputs):
    result = []
    for inp in inputs:
        total_len = 0
        for i in range(len(inp)):
            suffix = inp[i:]
            suffix_len = 0
            for j in reversed(range(len(suffix))):
                tochk = suffix[0:j+1]
                if inp.startswith(tochk):
                    suffix_len = len(tochk)
                    break
            total_len += suffix_len
        result.append(total_len)
    return result




if __name__ == '__main__':
    input = ['abcabcd']
    commonPrefix(input)

