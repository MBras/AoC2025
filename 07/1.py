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

# recursive now
# start from  S
height, width = tree.shape
print(tree.shape)

rectree = np.zeros(tree.shape)
print(rectree)

s = np.argwhere(tree == "S")[0]

def splitter(start):
    if rectree[start[0], start[1]] != 0:
        return rectree[start[0], start[1]]
    # if the bottom is reached, done
    elif start[0] + 1 == len(tree):
        rectree[start[0], start[1]] = 1
        return 1
    # if a "^" is encountered, split the beam
    elif tree[start[0] + 1, start[1]] == "^":
        value = splitter([start[0] + 1, start[1] - 1]) + splitter([start[0] + 1, start[1] + 1])
        rectree[start[0], start[1]] = value
        return value
    else:
        value = splitter([start[0] + 1, start[1]])
        rectree[start[0], start[1]] = value
        return value

print("Part 2:")
print(splitter(s))
print(rectree)
