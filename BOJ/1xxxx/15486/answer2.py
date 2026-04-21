def main():
    I=open(0).readline
    n=int(I())
    t=[]
    p=[]
    dp=[0]*(n+1)
    for _ in range(n):
        a,b=map(int,I().split())
        t.append(a)
        p.append(b)
    for i in range(n-1,-1,-1):
        if i+t[i]>n:dp[i]=dp[i+1]
        else:dp[i]=max(p[i]+dp[i+t[i]],dp[i+1])
    print(dp[0])
main()