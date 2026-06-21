from collections import deque
import sys

def main():
    input=sys.stdin.readline
    n,k=map(int,input().split())
    a=sorted([tuple(map(int,input().split()))for _ in range(n)],key=lambda x:x[1])
    
    left,right=0,10**9
    ans=0
    while left<=right:
        mid=(left+right)//2
        
        count=1
        tempr=a[0][1]
        for i in range(1,n):
            l,r=a[i]
            if l>=tempr+mid:
                tempr=r
                count+=1
        
        if count>=k:
            ans=mid
            left=mid+1
        else:
            right=mid-1
            
    print(ans if ans else -1)


main()