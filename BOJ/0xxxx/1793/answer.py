def main():
    dp=[1,1,3]
    for i in range(3,251):
        dp.append(dp[i-1]+2*dp[i-2])
    r=[]
    for n in map(int,open(0)):
        r.append(str(dp[n]))
    open(1,'w').write('\n'.join(r))
    
main()