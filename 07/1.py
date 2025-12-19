import sys
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

tree = np.array([list(line.strip()) for line in open(filename, 'r').readlines()])

c = 0
for y in range(len(tree)):
    for x in range(len(tree[y])):
        # check the cell above
        if tree[y - 1, x] in ["S", "|"]:
            if tree[y, x] == ".":
                tree[y, x] = "|"
            elif tree[y, x] == "^":
                # split beam
                tree[y, x - 1] = "|"
                tree[y, x + 1] = "|"
                c += 1
print(tree)
print(c)
