'''
For this challenge, you will need to parse data from STDIN to find a character in a matrix. Below is an example of the input you will receive from STDIN:
 
[2, 4]
AFKPU
BGLQV
CHMRW
DINSX
EJOTY
 
The first line is the [X, Y] coordinates of the character in the matrix ([0, 0] is the bottom left character). The remaining lines contain a matrix of random characters, with a character located at the coordinates from line 1.
So, in the example above, we're looking for a character at the coordinates [2, 4]. Moving right 2 spaces, and up 4, we find the character K. So, K is the character.
 
Please write a program that reads from STDIN and prints the answer to STDOUT. Use the "Run Tests" button to check your solution against the test cases.


# Enter your code here. Read input from STDIN. Print output to STDOUT

'''

import fileinput

if __name__ == '__main__':
    line_num = 0
    coordinate = ''
    characters = []
    for line in fileinput.input():
        if line_num == 0:
            coordinate = line
        else: 
            characters.append(line)
        line_num = line_num + 1
    splitted = coordinate.split(',')
    x_cord = int(splitted[0][1:])
    y_cord = int(splitted[1][1].strip())
    #print(x_cord)
    #print(y_cord)
    #print(characters[len(characters)-1-y_cord])
    print(characters[len(characters)-1-y_cord][x_cord])