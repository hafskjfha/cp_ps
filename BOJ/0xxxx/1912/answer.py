def main():
    dp=[float('-inf')]*(int(input())+1)
    for i,n in enumerate(map(int,input().split()),1):
        dp[i]=max(dp[i-1]+n,n)
    print(max(dp))
main()