s=set()
for x in map(str.strip,open(0)):
    if x in s:s.remove(x)
    else:s.add(x)
print(*s)