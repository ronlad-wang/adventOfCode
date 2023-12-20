import re
file_path = './day_08/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

steps = Lines[0]
directions = [0] * 17576
for i in range(2, len(Lines)):
    index = int(ord(Lines[i][0]) - 65 + 26 * (ord(Lines[i][1]) - 65) + 26**2 * (ord(Lines[i][2]) - 65))
    directions[index] = (Lines[i][7:10], Lines[i][12:15])


num_steps = 0
curr = "AAA"
while not curr == "ZZZ":
    print(curr, end = ' ')
    curr_index = int(ord(curr[0]) - 65 + 26 * (ord(curr[1]) - 65) + 26**2 * (ord(curr[2]) - 65))
    if steps[num_steps % (len(steps)-1)] == "L":
        curr = directions[curr_index][0]
    else:
        curr = directions[curr_index][1]
    num_steps += 1
print(curr, end=' ')
print(num_steps)
