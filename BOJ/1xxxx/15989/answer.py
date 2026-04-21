I=open(0).readline
n=10001
dp=[1]*(n)
for i in range(2,n):dp[i]+=dp[i-2]
for i in range(3,n):dp[i]+=dp[i-3]
for _ in range(int(I())):print(dp[int(I())])