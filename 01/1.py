import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

instructions = [(line[0], int(line[1:])) for line in open(filename, 'r').readlines()]

dial = 50
counter = 0
for i in instructions:
    dial += i[1] if i[0] == "R" else -i[1]
    if dial % 100 == 0:
        counter += 1

#1
print(counter)

#2
dial = 50
counter2 = 0
for i in instructions:
    for _ in range(i[1]):
        dial += 1if i[0] == "R" else -1
        if dial % 100 == 0:
            counter2 += 1

print(counter2)
