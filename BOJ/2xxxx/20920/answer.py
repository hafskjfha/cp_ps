input=open(0).readline
n,m=map(int,input().split())
w=[x for _ in range(n)if len(x:=input().strip())>=m]
c={}
for x in w:c[x]=c.get(x,0)+1
print(*sorted(c.keys(),key=lambda x:(-c[x],-len(x),x)))