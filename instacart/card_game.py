'''
Card game
 
You will be building a program to play a card game. The objective of the game is to form a hand of three cards that for
each of three different properties are either all the same or all different.
 
The properties of a card are:
1. Prefix: +, -, or =
2. Letter:  A ,  B , or  C 
3. Number of letters: 1, 2, or 3 (eg A, AA, AAA)
 
For example, given the following set of cards
-A -B -BB +C -C -CC =CCC
there are two possible hands:
 
+C -CC =CCC 1.
    Prefix: + , -, = | All different 
    Letter: C, C, C | All same 
    Number of letters: 1, 2, 3 | All different
 
-A -B -C 1.
    Prefix: -, -, - | All same 
    Letter: A, B, C | All different 
    Number of letters: 1, 1, 1 | All same
 
Specifications
– You only need to find one hand – The cards should be read from STDIN, each card is separated by a space
– Print the hand you find to STDOUT, space separated (trailing space is ok)
– Cards may appear in any order in the input
– Cards may be output in any order
– Use the "Run Tests" button to check your solution as often as you like
'''

from itertools import permutations
import fileinput, sys

def check_all_same_or_different(prop_1, prop_2, prop_3):
    s = set([prop_1, prop_2, prop_3])
    return len(s) == 1 or len(s) == 3

def check_sign_property(card1, card2, card3):
    return ((card1[0] == card2[0]) and (card2[0] == card3[0])) or ((card1[0] != card2[0]) and (card2[0] != card3[0]) and (card3[0] != card1[0]))

def check_letter_property(card1, card2, card3):
    return ((card1[1] == card2[1]) and (card2[1] == card3[1])) or ((card1[1] != card2[1]) and (card2[1] != card3[1]) and (card3[1] != card1[1]))
    
def check_letter_number_property(card1, card2, card3):
    card1_number = len(card1) - 1
    card2_number = len(card2) - 1
    card3_number = len(card3) - 1
    
    return ((card1_number == card2_number) and (card2_number == card3_number)) or ((card1_number != card2_number) and (card2_number != card3_number) and (card3_number != card1_number))
    
def calculate_win(perm):
    card_1 = perm[0]
    card_2 = perm[1]
    card_3 = perm[2]

    if ((check_all_same_or_different(card_1[0], card_2[0], card_3[0])) and
            (check_all_same_or_different(card_1[1], card_2[1], card_3[1])) and
            (check_all_same_or_different(len(card_1)-1, len(card_2)-1, len(card_3) -1))): #-1 to subtract for the sign at the start.
            return [card_1, card_2, card_3]

if __name__ == '__main__':
        for line in fileinput.input():
            cards = line.split(' ')
            for item in permutations(cards, 3):
                result = calculate_win(item)
                if result:
                    print("%s %s %s" % (result[0], result[1], result[2]))
                    sys.exit(0)

