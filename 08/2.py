import sys
import math
import itertools
from collections import Counter

# Check if the filename is provided
if len(sys.argv) < 3:
    print("Usage: python 1.py <filename> <connections>")
    sys.exit(1)

# Get the filename from the command line arguments
filename = sys.argv[1]
connections = int(sys.argv[2])

boxes =  [[int(c) for c in line.split(",")] for line in open(filename, 'r').readlines()]

def distance(b1, b2):
    return math.sqrt((b1[0] - b2[0])**2 + (b1[1] - b2[1])**2 + (b1[2] - b2[2])**2)

combos = list(itertools.combinations(boxes, 2))

distances = dict()
for combo in combos:
    #print(combo)
    #print(distance(combo[0], combo[1]))
    distances[distance(combo[0], combo[1])] = combo

toconnect = list(dict(sorted(distances.items())).items())

# networks
net = dict()
nc = 0
nc2 = 0

for con in toconnect:
    print(con)
    c1 = ",".join(map(str, con[1][0]))
    c2 = ",".join(map(str, con[1][1]))
    
    # check if connection one already in a network
    if c1 in net:
        # check if connection two is in a network
        if c2 in net:
            # check if the networks are the same, if yes, do nothing
            if net[c1] == net[c2]:
                print("Same network")
            else:
                print("Merging networks")
                # if no, merge the two networks
                check = net[c2]
                for k, v in net.items():
                    if v == check:
                        net[k] = net[c1]

                # reduce number of networks:
                nc2 -= 1

        # if not, add the connection to the network of connection one
        else:
            print("Adding c2 to net 1")
            net[c2] = net[c1]
    # if connection one is not in a network
    else:
        # check if connection two is in a network
        if c2 in net:
            print("Adding c1 to net 2")
            # add connection one to the network of connection two
            net[c1] = net[c2]
        
        # start a new network with the two connections
        else:
            print("Creating new network")
            net[c1] = nc
            net[c2] = nc
            nc += 1
            nc2 += 1

    # check endstate
    if nc2 == 1 and len(boxes) == len(net):
        print("To connect: " + str(len(boxes)))
        print("Connect:    " + str(len(net)))
        print("Part 2: " +str(int(c1.split(",")[0]) * int(c2.split(",")[0])))
        break

