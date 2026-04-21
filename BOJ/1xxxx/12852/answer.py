def main():
    n=int(input())
    dp=[0]*(n+1)
    back=[0]*(n+1)
    for i in range(2,n+1):
        t,m=i-1,dp[i-1]
        if i%3==0 and dp[i//3]<m:
            m=dp[i//3]
            t=i//3
        if i%2==0 and dp[i//2]<m:
            m=dp[i//2]
            t=i//2
        dp[i]=m+1
        back[i]=t
    print(dp[n])
    cur=n
    while cur>0:
        print(cur,end=' ')
        cur=back[cur]
main()