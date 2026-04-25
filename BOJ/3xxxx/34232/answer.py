def main():
    input=open(0).readline
    n=int(input())
    nums=[None]*(n**2+1)
    board=[]
    for y in range(n):
        b=[*map(int,input().split())]
        for x in range(n):
            nums[b[x]]=(x,y)
    x1,y1=nums[1]
    x2,y2=nums[1]
    ans=0
    for k in range(1,n**2+1):
        x,y=nums[k]
        x1,y1=min(x1,x),min(y1,y)
        x2,y2=max(x2,x),max(y2,y)
        if k==(x2-x1+1)*(y2-y1+1):
            ans+=1
    print(ans)
main()
    