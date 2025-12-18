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


c2 = 0
for bank in banks:
    joltage = 0
    nb = 12
    p = 0 

    # get max in the first x digits
    for _ in range(nb):
        if nb == 1:
            #print(bank[p:])
            pos, val = max(enumerate(bank[p:]), key=lambda x: x[1])
        else:
            #print(bank[p:-nb + 1])
            pos, val = max(enumerate(bank[p:-nb + 1]), key=lambda x: x[1])
        #print(pos)
        nb -= 1
        p += pos + 1
        joltage = joltage * 10 + val
    #print(joltage)
    c2 += joltage

print("Part 2:")
print(c2)
print(banks[0][3:0])   
