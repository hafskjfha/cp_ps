def main():
    from math import log2,ceil
    n=int(input())
    a=[*map(int,input().split())]
    dp=[0]*n
    c=0
    for i in range(1,n):
        n=max(0,ceil(log2(a[i-1])-log2(a[i])) + dp[i-1])
        dp[i]=n        
        c+=n
    print(c)
main()