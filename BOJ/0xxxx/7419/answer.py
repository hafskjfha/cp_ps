I=open(0).readline
n,k=map(int,I().split())
c=[float(I())*100 for _ in range(n)]
a=0
l,r=1,max(c)
while l<=r:
    mid=(l+r)//2
    if sum(x//mid for x in c)>=k:
        a=mid/100
        l=mid+1
    else:
        r=mid-1
print(f"{a:.2f}")