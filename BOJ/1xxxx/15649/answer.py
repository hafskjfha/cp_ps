n,m=map(int,input().split())
print=open(1,'w').write
r=[]
def back(s):
    if len(s)==m:
        r.append(' '.join(map(str,s)))
        return

    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            back(s)
            s.pop()

for j in range(1,n+1):
    back([j])
print('\n'.join(r))