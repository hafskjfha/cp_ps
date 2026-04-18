def main():
    input=open(0).readline
    r=[]
    for _ in range(int(input())):
        n=int(input())
        sticker=[[*map(int,input().split())] for _ in "__"]
        dp=[[0]*n for _ in "__"]
        if n==1: 
            r.append(str(max(sticker[0][0],sticker[1][0])))
            continue

        dp[0][0]=sticker[0][0]
        dp[1][0]=sticker[1][0]
        dp[0][1]=sticker[0][1]+dp[1][0]
        dp[1][1]=sticker[1][1]+dp[0][0]

        for i in range(2,n):
            dp[0][i]=max(dp[1][i-1],dp[1][i-2])+sticker[0][i]
            dp[1][i]=max(dp[0][i-1],dp[0][i-2])+sticker[1][i]
            
        r.append(str(max(dp[0][n-1],dp[1][n-1])))
        
    print(' '.join(r))

main()