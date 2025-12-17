import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

ranges =  [[int(i) for i in r.split("-")] for r in open(filename, 'r').readlines()[0].split(",")]

c = 0
for r in ranges:
    for i in range(r[0], r[1] + 1):
        s = str(i)
        mid = len(s) // 2
        if s[:mid] == s[mid:]:
            #print(i)
            c += i
print("Part 1: ")
print(c)    
