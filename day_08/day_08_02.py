import re
import numpy
file_path = './day_08/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

steps = Lines[0]
directions = [0] * 17576
starting_points = []
for i in range(2, len(Lines)):
    index = int(ord(Lines[i][0]) - 65 + 26 * (ord(Lines[i][1]) - 65) + 26**2 * (ord(Lines[i][2]) - 65))
    directions[index] = (Lines[i][7:10], Lines[i][12:15])
    if Lines[i][2] == "A":
        starting_points.append(Lines[i][0:3])


print(starting_points)
print("hi")



all_at_z = False
steps_counts = []

for i in range(len(starting_points)):
    num_steps = 0
    curr = starting_points[i]
    while not curr[2] == 'Z':
        curr_index = int(ord(curr[0]) - 65 + 26 * (ord(curr[1]) - 65) + 26**2 * (ord(curr[2]) - 65))
        if steps[num_steps % (len(steps)-1)] == "L":
            curr = directions[curr_index][0]
        else:
            curr = directions[curr_index][1]
        starting_points[i] = curr
        num_steps += 1
    steps_counts.append(num_steps)
    


print(steps_counts)
print(numpy.lcm.reduce(steps_counts))
        


