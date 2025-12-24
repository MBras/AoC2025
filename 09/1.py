import sys
import itertools

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

coords =  [[int(c) for c in line.split(",")] for line in open(filename, 'r').readlines()]
print(coords)

def surface(c1, c2):
    return ((abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)) 

combos = list(itertools.combinations(coords, 2))

maxsurface = 0
for c in combos:
    s = surface(c[0], c[1])
    if s > maxsurface:
        print(c)
        print(s)
        maxsurface = s
