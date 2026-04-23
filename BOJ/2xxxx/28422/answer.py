n=int(input())
a=[*map(int,input().split())]
dp=[-1]*(n+1)
dp[0]=0
for i in range(2,n+1):
    t2=t3=-1
    if dp[i-2]!=-1:
        t2=dp[i-2]+(a[i-1]^a[i-2]).bit_count()
    if dp[i-3]!=-1:
        t3=dp[i-3]+(a[i-1]^a[i-2]^a[i-3]).bit_count()
    dp[i]=max(t2,t3)
print(max(dp[-1],0))