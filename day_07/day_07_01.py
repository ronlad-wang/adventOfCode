class Hand:
    value = 0
    cards = ""
    self_class = 0
    def __init__(self, cards, value):
        self.cards = cards
        self.value = value
        self.sort_val = []
        self.self_class = self.findclass()
    
    def findclass(self):
        values = [0] * 15
        for i in range(len(self.cards)):
            c = self.cards[i]
            if c == 'T':
                c = 10
            elif c == 'J':
                c = 11
            elif c == 'Q':
                c = 12
            elif c == 'K':
                c = 13
            elif c == 'A':
                c = 14
            else:
                c = int(c)
            self.sort_val.append(c)
            values[c] += 1

        rank = 0
        for i in range(len(values)):
            rank += 10**values[i]
        
        if rank > 99999:
            return 7
        if rank > 9999:
            return 6
        if rank > 1099:
            return 5
        if rank > 999:
            return 4
        if rank > 199:
            return 3
        if rank > 99:
            return 2
        return 1
            
    def printself(self):
        print(self.value)
        print(self.cards)
        print(self.self_class)

def custom_compare(hand):
    return (hand.self_class, hand.sort_val[0], hand.sort_val[1], hand.sort_val[2], hand.sort_val[3], hand.sort_val[4])

import re
import math
file_path = './day_07/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

hands = []

for line in Lines:
    cards = line[0:5]
    value = line[6:]
    hands.append(Hand(cards, value))

sorted_objects = sorted(hands, key = custom_compare)

sum = 0
for i in range(len(sorted_objects)):
    obj = sorted_objects[i]
    print(obj.cards)
    print(int(obj.value))
    sum += int(obj.value) * (i+1)

print(sum)



