import re
import sys
file_path = './day_04/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

sum = 0

num_wins = [0] * len(Lines)

#use the same idea from pt 1 to count the number of wins
for i in range(len(Lines)):
    line = Lines[i]
    matches = re.finditer(r"[0-9]+", line[9:])
    winning = []
    j = 0
    total_winning = 0
    for match in matches:
        if j < 10:
            winning.append(int(line[match.start() + 9:match.end() + 9]))
            j += 1
        else:
            if int(line[match.start() + 9:match.end() + 9]) in winning:
                total_winning += 1

    num_wins[i] = total_winning
    
#next we'll use a simple dynamic programming method to count the number of each ticket we have
num_tickets = [1] * len(Lines)

for i in range(len(num_wins)):
    for j in range(num_wins[i]):
        num_tickets[i + j + 1] += num_tickets[i]
    
#count the total number of tickets
for i in range(len(num_tickets)):
    sum += num_tickets[i]

print(sum)