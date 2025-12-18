import sys
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

warehouse = np.pad(np.array([list(line.strip()) for line in open(filename, 'r').readlines()]), pad_width=1, mode="constant", constant_values=".")
print(warehouse)

c = 0
for y in range(1, len(warehouse) - 1):
    for x in range(1, len(warehouse[0]) - 1):
        if warehouse[x, y] == "@":
            i = warehouse[x - 1: x + 2, y - 1: y + 2]
            if (i == "@").sum() < 5: # include the roll at pos x, y
                print(i)
                c +=1
print("Part 1:")
print(c)

# part 2



