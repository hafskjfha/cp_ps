n,d=map(int,input().split())
c=[*map(int,[input()for _ in range(n)])]
p=d//sum(c)
for x in c:print(x*p)