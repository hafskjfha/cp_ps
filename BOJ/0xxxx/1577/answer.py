def main():
    input=__import__('sys').stdin.readline
    n,m=map(int,input().split())
    dp=[[0]*(n+1) for _ in range(m+1)]
    dp[0][0]=1
    if n>1:
        dp[0][1]=1
    if m>1:
        dp[1][0]=1

    k=int(input())
    h=set()
    for _ in range(k):
        a,b,c,d=map(int,input().split())
        h.add(((a,b),(c,d)))

    for x in range(n+1):
        for y in range(m+1):
            if x==y==0:
                continue
            i=j=0
            if ((x-1,y),(x,y)) not in h and ((x,y),(x-1,y)) not in h:
                i=dp[y][x-1]
            if ((x,y-1),(x,y)) not in h and ((x,y),(x,y-1)) not in h:
                j=dp[y-1][x]
            dp[y][x]=i+j
    print(dp[m][n])  

main()