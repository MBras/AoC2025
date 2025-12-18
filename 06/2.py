import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

lines = open(filename, 'r').readlines()
ops = lines[len(lines) - 1].split()

vals = []
values = []
col = 0
for x in range(len(lines[0]) - 1):
    val = 0
    for y in range(len(lines) - 1):
        c = lines[y][x]
        if c != " ":
            val = val * 10 + int(c)
    if val == 0:
        values.append(vals)
        vals = []
        col += 1
    else:
        vals.append(val)
values.append(vals)

result = 0
for i in range(len(ops)):
    print(i)
    if ops[i] == "+":
        r = 0
        for x in values[i]:
            r += x
        result += r
    elif ops[i] == "*":
        r = 1
        for x in values[i]:
            r *= x
        result += r
print(result)
