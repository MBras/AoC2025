import sys

# Check if the filename is provided
if len(sys.argv) < 2:
    print("Usage: python 1.py <filename>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]

ranges = []
ingredients = []
rr = 1
for line in open(filename, 'r').readlines():
    if line.strip() == "":
        rr = 0
    elif rr == 1:
        ranges.append([int(i) for i in line.split("-")])
    else:
        ingredients.append(int(line))

c = 0
for i in ingredients:
    found = False
    for r in ranges:
        if r[0] <= i and i <= r[1]:
            found = True
            break
    if found:
        c += 1
print("Part 1:")
print(c)

# find overlapping ranges
merged = []
for start, end in sorted(ranges):
    if not merged or start > merged[-1][1]:
       merged.append([start, end])
    else:
       merged[-1][1] = max(merged[-1][1], end)

c = 0
for m in merged:
    c += m[1] - m[0] + 1

print("Part 2:")
print(c)
