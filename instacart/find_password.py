'''
This challenge builds off of the previous one. Please feel free to copy/paste from the previous challenge.
 
For this challenge, the goal is to construct a password from a series of chunks. The chunks will now look like:
 
1
[5, 6]
RXIBDIBF
DVMPXTBG
BMWAERXR
UPEIJGMW
YTALDXDH
JNPMOUEJ
XDRHCHWG

0
[0, 1]
HUTQW3
NLEVCU
You will notice each chunk looks similar to the previous challenge with one addition — the first line is the (0-based) index of the password character.
 
In our example – First chunk: password character index 1, character at [5, 6] is I – Second chunk: password character index 0, character at [0, 1] is H
 
Once you have processed all of the chunks you have the entire password and should print it to STDOUT. In our example the password is HI.
 
Chunks are separated by empty lines.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

def calculate_result(x_cord, y_cord, characters):
    return characters[len(characters)-1-y_cord][x_cord]

def process_chunk(lines, password_chars):
    line_num = 0
    coordinate = ''
    characters = []
    password_index = ''

    for line in lines:
        if line_num == 0:
            password_index = int(line)
        elif line_num == 1:
            coordinate = line
        else:
            characters.append(line)
        line_num = line_num +1

    splitted = coordinate.split(',')
    x_cord = int(splitted[0][1:])
    y_cord = int(splitted[1][1].strip())
    password_chars[password_index] = calculate_result(x_cord, y_cord, characters)

if __name__ == '__main__':
    lines = ["1", "[5, 6]", "RXIBDIBF", "DVMPXTBG","BMWAERXR","UPEIJGMW", "YTALDXDH", "JNPMOUEJ","XDRHCHWG", "\n", "0", "[0, 1]", "HUTQW3", "NLEVCU"]
    password_chars = {}

    sub_lines = []
    for item in lines:
        if not item == '\n':
            sub_lines.append(item)
        else:
            process_chunk(sub_lines, password_chars)
            sub_lines = []

    if sub_lines:
        process_chunk(sub_lines, password_chars)
    result=''
    for i in range(len(password_chars)):
        result += password_chars[i]
    print(result)