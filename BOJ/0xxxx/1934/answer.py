from math import lcm
for x in [*open(0)][1:]:
    print(lcm(*map(int,x.split())))