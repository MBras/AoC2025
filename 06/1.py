import sys
import numpy as np

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

problems =  np.array([line.split() for line in open(filename, 'r').readlines()])
problems[:len(problems) - 1] =  problems[:len(problems) - 1].astype(int)

height, width = problems.shape
result = 0
for x in range(width):
    op = problems[height - 1, x]
    vals = problems[0:height -1 , x].astype(int)
    print(vals)
    if op == "+":
        result += vals.sum()
        print(vals.sum())
    elif op == "*":
        print(vals.prod())
        result += vals.prod()

print("Part 1:")
print(result)

