def moves(commands, word):
    cursor = 0
    com = None
    i = 0
    while i < len(commands):

        command_i = commands[i]
        if command_i == 'h' or command_i == 'l':
            com = command_i
            i += 1
        elif command_i == 'r':
            com = commands[i:i+2]
            i += 2
        elif isinstance(int(command_i), int):
            num_start_index = i

            while(True):
                try:
                    isinstance(int(commands[num_start_index]), int)
                except ValueError:
                    break
                num_start_index += 1
            num_com = commands[i: num_start_index]
            i = num_start_index

            if commands[i] == 'h' or commands[i] == 'l':
                # 2h or 2l
                com = num_com + commands[i]
                i += 1
            elif commands[i] == 'r':
                com = num_com + commands[i:i+2]
                i += 2
        print(com)

def run_command(command, word, cursor):
    # (word, cursor_position)
    cur = cursor
    if command == 'h':
        cur = cur - 1
        if cur < (-1 * len(word)):
            cur = -1
        return (word, cur)
    elif command == 'l':
        cur = cur + 1
        if cur == len(word):
            cur = 0
        return (word, cur)

    elif len(command) == 2 and command[0] == 'r':
        char_to_replace = command[1]
        new_word = word[:cursor] + char_to_replace + word[cursor+1 :]
        return (new_word, cursor)


if __name__ == '__main__':
    #moves('999999999lr0', 'Hello World')
    moves('999rs', 'H')