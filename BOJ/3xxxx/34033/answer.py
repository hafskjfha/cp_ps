I=open(0).readline
n,m=map(int,I().split())
d={}
a=0
for _ in range(n):
    x,y=I().split()
    d[x]=int(y)
for _ in range(m):
    x,y=I().split()
    if d[x]*1.05<int(y):a+=1
print(a)