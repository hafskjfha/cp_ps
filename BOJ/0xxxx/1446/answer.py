I=open(0).readline
n,d=map(int,I().split())
sh={}
for _ in range(n):
    a,b,h=map(int,I().split())
    sh.setdefault(b,[]).append((a,h))
dp=[0]*(d+1)
for i in range(1,d+1):
    t=dp[i-1]+1
    for y,h in sh.get(i,[]):t=min(t,dp[y]+h)
    dp[i]=t
print(dp[-1])