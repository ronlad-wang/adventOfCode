import re
import sys
file_path = './day_03/q1.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()
pattern = "[0-9]+"

#main idea is to use gear_locations, a dictionary, to keep track of the coordinates of each gear and what
#parts are adjacent to it
gear_locations = {}

for i in range(len(Lines)):
    line = Lines[i]
    matches = re.finditer(pattern, line)
    for match in matches:
        s = match.start()
        e = match.end()
        seen = {}
        for h in range(s, e):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if i + j < 0 or i + j >= len(Lines) or h + k < 0 or h + k >= 140:
                        continue
                    
                    
                    if not i+j in seen:
                        seen[i+j] = []

                    #we've slightly modified the code from part 1 to now find all of the stars
                    if re.match(r"\*", Lines[i + j][h + k]) and not h+k in seen[i+j]:
                        #adds the gear's coordinates, where x is the key of the first dict
                        #and y is the key of the second dict
                        if not i+j in gear_locations:
                            gear_locations[i+j] = {}

                        if not h+k in gear_locations[i+j]:
                            gear_locations[i+j][h+k] = []
                        
                        #then at x,y there is a list that contains the part numbers adjacent to the gear
                        gear_locations[i+j][h+k].append(line[s:e])

                    #seen solves the problem where we may add the same part to the gear array multiple times
                    #this makes it so that parts we've already considered cannot be readded
                    if not h+k in seen[i+j]:
                        seen[i+j].append(h+k)
        
        
sum = 0

#finally, take all of the gears and check how many parts they are adjacent to, then find the sum.
for i in gear_locations.keys():
    for j in gear_locations[i].keys():
        gear_adjacencies = gear_locations[i][j]
        if len(gear_adjacencies) == 2:
            sum += int(gear_adjacencies[0]) * int(gear_adjacencies[1])
        
print(sum)

