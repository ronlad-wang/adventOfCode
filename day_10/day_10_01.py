file_path = './day_10/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

first_coord = 0
sec_coord = 0
for i in range(len(Lines)):
    for j in range(len(Lines[i])):
        if Lines[i][j] == "S":
            first_coord = i
            sec_coord = j

#this is slightly cheating, looking at the input we see that the first step we can always take is to go up
prev_first_coord = first_coord
prev_sec_coord = sec_coord
first_coord = first_coord - 1


total_steps = 1
while not Lines[first_coord][sec_coord] == "S":
    curr = Lines[first_coord][sec_coord]
    total_steps += 1
    print(curr)
    if curr == "|":
        if prev_first_coord > first_coord:
            prev_first_coord = first_coord
            first_coord -= 1
        else:
            prev_first_coord = first_coord
            first_coord += 1
    if curr == "-":
        if prev_sec_coord < sec_coord:
            prev_sec_coord = sec_coord
            sec_coord += 1
        else: 
            prev_sec_coord = sec_coord
            sec_coord -= 1
    if curr == "J":
        if prev_first_coord < first_coord:
            prev_first_coord = first_coord
            sec_coord -= 1
        else:
            prev_sec_coord = sec_coord
            first_coord -= 1
    if curr == "7":
        if prev_first_coord > first_coord:
            prev_first_coord = first_coord
            sec_coord -= 1
        else:
            prev_sec_coord = sec_coord
            first_coord += 1
    if curr == "F":
        if prev_first_coord > first_coord:
            prev_first_coord = first_coord
            sec_coord += 1
        else:
            prev_sec_coord = sec_coord
            first_coord += 1
    if curr == "L":
        if prev_first_coord < first_coord:
            prev_first_coord = first_coord
            sec_coord += 1
        else:
            prev_sec_coord = sec_coord
            first_coord -= 1


print(total_steps/2)