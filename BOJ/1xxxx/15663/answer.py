n,m=map(int,input().split())
a=sorted(map(int,input().split()))
r=[]
v=[0]*n
def back(s):
    if len(s)==m:
        r.append(' '.join(map(str,s)))
        return
    b=0
    for i in range(n):
        if not v[i] and a[i] != b:
            v[i]=1
            s.append(a[i])
            back(s)
            b=a[i]
            v[i]=0
            s.pop()
back([])
print('\n'.join(r))
        