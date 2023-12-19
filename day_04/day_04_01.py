import re
import sys
file_path = './day_04/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

sum = 0

for line in Lines:
    #everything is offset by 9 because there are 9 characters at the beginning detailing the number of the card
    matches = re.finditer(r"[0-9]+", line[9:])

    #goal is to use finditer to find all of the numbers. We know that the first 10 are winning numbers
    #and the rest are the ones that represent what we have
    winning = []
    i = 0
    total_winning = 0
    for match in matches:
        if i < 10:
            #keep track of our winning numbers
            winning.append(int(line[match.start() + 9:match.end() + 9]))
            i += 1
        else:
            #compare the numbers we have to the winning numbers
            if int(line[match.start() + 9:match.end() + 9]) in winning:
                total_winning += 1

    if(total_winning > 0):
        sum += 2**(total_winning-1)

print(sum)