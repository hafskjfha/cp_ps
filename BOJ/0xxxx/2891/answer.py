n,s,r=map(int,input().split())
w={*map(int,input().split())}
g={*map(int,input().split())}
gg=g-w
w=w-g
for x in sorted(gg):
    if x in w:
        w.remove(x)
        continue
    if x>1 and x-1 in w:
        w.remove(x-1)
    elif x<n and x+1 in w:
        w.remove(x+1)
print(len(w))