INF=float('inf')
n=int(input())
cost=[[*map(int,input().split())]for _ in range(n)]
dp=[[[INF]*3 for _ in range(3)]for _ in range(n)]
dp[0]=[[cost[0][i]if i==j else INF for j in range(3)] for i in range(3)]
for j in range(3):
    for i in range(1,n):
        dp[i][j][0]=min(dp[i-1][j][1],dp[i-1][j][2])+cost[i][0]
        dp[i][j][1]=min(dp[i-1][j][0],dp[i-1][j][2])+cost[i][1]
        dp[i][j][2]=min(dp[i-1][j][0],dp[i-1][j][1])+cost[i][2]
print(min(dp[-1][i][j]for j in range(3)for i in range(3)if i!=j))