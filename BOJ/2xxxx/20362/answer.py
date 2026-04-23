n,s=input().split()
d={}
for _ in range(int(n)):
    p,a=input().split()
    if p==s:exit(print(d.get(a,0)))
    d[a]=d.get(a,0)+1