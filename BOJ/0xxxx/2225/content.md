n,k=map(int,input().split())
mod=1000000000
dp=[[0]*(k+1) for _ in range(n+1)]
dp[0]=[1]*(k+1)
for i in range(1,n+1):
    for j in range(1,k+1):
        for l in range(i+1):
            dp[i][j]=(dp[i][j]+dp[i-l][j-1])%mod
print(dp[n][k])