n,_=map(int,input().split())
a=[*map(int,input().split())]
d={}
p={}
for i in range(n):
    x=a[i]
    d[x]=d.get(x,0)+1
    if p.get(x)is None:p[x]=i
for k in sorted(d.keys(),key=lambda x:(-d[x],p[x])):print(*[k]*d[k],end=' ')