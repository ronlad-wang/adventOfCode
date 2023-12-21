file_path = './day_11/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

empty_rows = [False] * len(Lines)
empty_cols = [False] * (len(Lines[0]) - 1)

for i in range(len(Lines)):
    empty = True
    for j in range(len(Lines[i])):
        if Lines[i][j] == "#":
            empty = False
            break
    if empty:
        empty_rows[i] = True

for i in range(len(Lines[0]) - 1):
    empty = True
    for j in range(len(Lines)):
        if Lines[j][i] == "#":
            empty = False
            break
    if empty:
        empty_cols[i] = True

print(empty_rows)
print(empty_cols)
if empty_rows[0]:
    empty_rows[0] = 1
else:
    empty_rows[0] = 0

if empty_cols[0]:
    empty_cols[0] = 1
else:
    empty_cols[0] = 0

for i in range(1, len(empty_rows)):
    if empty_rows[i]:
        empty_rows[i] = empty_rows[i-1] + 1
    else:
        empty_rows[i] = empty_rows[i-1]

for i in range(1, len(empty_cols)):
    if empty_cols[i]:
        empty_cols[i] = empty_cols[i-1] + 1
    else:
        empty_cols[i] = empty_cols[i-1]

print(empty_rows)
print(empty_cols)

star_coords = []
for i in range(len(Lines)):
    for j in range(len(Lines[0]) - 1):
        if Lines[i][j] == "#":
            star_coords.append((i + empty_rows[i], j + empty_cols[j]))

print(star_coords)

sum_dists = 0
for i in range(len(star_coords)):
    for j in range(len(star_coords)):
        if i == j:
            continue
        sum_dists += abs(star_coords[i][0] - star_coords[j][0])
        sum_dists += abs(star_coords[i][1] - star_coords[j][1])

print(sum_dists/2)

