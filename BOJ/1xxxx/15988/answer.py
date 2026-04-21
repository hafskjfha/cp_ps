def main():
    dp=[0]*1000000
    dp[0],dp[1],dp[2]=1,2,4
    for i in range(3,1000000):
        dp[i]=(dp[i-1]+dp[i-2]+dp[i-3])%int(1e9+9)
    r=[]
    for n in map(int,[*open(0)][1:]):
        r.append(str(dp[n-1]))
    import sys
    sys.stdout.write('\n'.join(r))
main()