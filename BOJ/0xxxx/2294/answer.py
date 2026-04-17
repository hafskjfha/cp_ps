def main():
    input=open(0).readline
    INF=float('inf')
    n,k=map(int,input().split())
    g=sorted(set(int(input())for _ in range(n)))
    dp=[INF]*(k+1)
    dp[0]=0
    for i in range(1,k+1):
        for j in g:
            if i-j<0: continue
            dp[i]=min(dp[i],dp[i-j]+1)
            
    print(dp[k] if dp[k]!=INF else -1)
main()