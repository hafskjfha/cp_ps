input=open(0).readline
n,m=map(int,input().split())
ll=[*map(int,input().split())]
for _ in range(m):
    c,i,x=map(int,input().split())
    if c==1:
        ll[i-1]=x
    elif c==2:
        for j in range(i-1,x):
            ll[j]=not ll[j]
    elif c==3:
        for j in range(i-1,x):
            ll[j]=False
    else:
        for j in range(i-1,x):
            ll[j]=True
print(*map(int,ll))