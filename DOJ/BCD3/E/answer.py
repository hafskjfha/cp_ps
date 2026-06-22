from bisect import bisect_left

def main():
    input=open(0).readline
    MOD=998244353
    n=int(input())
    t=[sorted(map(int,input().split()))for _ in range(3)]
    
    for i in range(3):
        ts=0
        for x in t[i]:
            ts+=bisect_left(t[[1,2,0][i]],x)*bisect_left(t[[2,0,1][i]],x)
        print((ts*pow(pow(n,3,MOD),-1,MOD))%MOD,end=' ')
    
    
    


main()