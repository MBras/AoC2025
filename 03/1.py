import sys
import heapq

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

banks =  [ list(map(int, line.strip())) for line in open(filename, 'r').readlines()]

c1 = 0
for bank in banks:
    # find highest number
    p1, val1 = max(enumerate(bank), key=lambda x: x[1])

    # if this is the last position, look back for next highest number
    if p1 == len(bank) - 1:
        val2 = max(bank[:-1])
        joltage = val2 * 10 + val1
    # otherwise look for the highest number in the remaining part
    else:
        val2 = max(bank[p1 + 1:])
        joltage = val1 * 10 + val2

    c1 += joltage

print("Part 1:")
print(c1)
