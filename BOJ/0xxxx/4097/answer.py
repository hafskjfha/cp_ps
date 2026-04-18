def main():
    input=map(int,open(0)).__next__
    r=[]
    while 1:
        n=input()
        if n==0: break
        dp=[float('-inf')]*n
        for i in range(n):
            a=input()
            if i!=0:
                dp[i]=max(dp[i-1]+a,a)
            else:
                dp[i]=a
        r.append(str(max(dp)))
    print('\n'.join(r))
main()