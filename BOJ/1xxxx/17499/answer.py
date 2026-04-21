input=open(0).readline
n,q=map(int,input().split())
a=[*map(int,input().split())]
s=0
for _ in range(q):
    c,i,*x=map(int,input().split())
    if c==1:a[(s+i-1)%n]+=x[0]
    elif c==2:s=(s-i)%n
    else:s=(s+i)%n
print(*a[s:],*a[:s])