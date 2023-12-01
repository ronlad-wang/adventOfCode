file_path = './day_01/q1.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    first = -1
    last = -1
    for i in range(len(line)):
        if line[i].isdigit():
            if first == -1:
                first = line[i]
            last = line[i]
    combined = str(first) + str(last)
    sum += int(combined)

print(sum)