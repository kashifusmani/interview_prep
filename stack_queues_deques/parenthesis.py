
def is_balanaced(input):
    s = []
    for item in input:
        if item == '(' or item == '{' or item == '[':
            s.append(item)
        else:
            if len(s) == 0:
                return False
            popped = s.pop()
            if item == '}' and not popped == '{':
                return False
            elif item == ')' and not popped == '(':
                return False
            elif item == ']' and not popped == '[':
                return False
    return len(s) == 0


def balance_check(input):
    if len(input) %2 != 0:
        return False
    opening = set('({[')
    matches = set([('(',')'),('[',']'),('{','}')])
    stack = []
    for item in input:
        if item in opening:
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            prev_open = stack.pop()
            if (prev_open, item) not in matches:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    print(is_balanaced('()(){]}'))
