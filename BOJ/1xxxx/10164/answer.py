n,m,k=map(int,input().split())
def f(dp,n,m,si=0,sj=0):
    dp[si][sj]=1
    for i in range(si,n):
        for j in range(sj,m):
            if i+1<n:dp[i+1][j]+=dp[i][j]
            if j+1<m:dp[i][j+1]+=dp[i][j]
if k:
    dp1=[[0]*m for _ in range(n)]
    dp2=[[0]*m for _ in range(n)]
    f(dp1,n,m)
    f(dp2,n,m,(k-1)//m,(k-1)%m)
    print(dp1[(k-1)//m][(k-1)%m]*dp2[-1][-1])
else:
    dp=[[0]*m for _ in range(n)]
    f(dp,n,m)
    print(dp[-1][-1])