def main():
    n=int(input())
    mod=int(1e9)
    dp=[[0]*10 for _ in range(n)]
    for i in range(1,10):
        dp[0][i]=1
    for i in range(1,n):
        dp[i][0]=dp[i-1][1]
        dp[i][9]=dp[i-1][8]
        for j in range(1,9):
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%mod
    print(sum(dp[n-1])%mod)
main()