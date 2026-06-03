def main():
    input=open(0).readline
    n,k=map(int,input().split())
    a=[*map(int,input().split())]
    ans=-1
    
    left,right=1,4*10**18
    while left<=right:
        mid=(left+right)//2
        temp=0
        
        for i in range(n):
            need = mid - a[i]
            if need > 0:
                temp += (need + i) // (i + 1)

            if temp > k:
                break
        
        if temp<=k:
            ans=mid
            left=mid+1
        else:
            right=mid-1
            
    print(ans)
        
        

main()