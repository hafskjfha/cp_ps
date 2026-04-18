d,l={},set()
for x in open(0):
    if x in d:l.add(x)
    if x not in d:d[x]=1
print(''.join(sorted(l)).strip())