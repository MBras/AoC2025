import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

lines = open(filename, 'r').readlines()

# read the input into a dictionary
devices = dict()
for line in lines:
    d, c = line.split(": ")
    cons = c.strip().split(" ")
    devices[d] = cons

def findpath(start, path):
    global counter

    for c in devices[start]:
        p = list(path)
        p.append(c)
        if c == "out":
            print(p)
            counter += 1
        else:
            findpath(c, p)

counter = 0
findpath("you", ["you"])
print(counter)
