n=int(input())
a=sorted(map(int,input().split()))
t=int(input())
i,j=0,n-1
r=0
while i<j:
    v=a[i]+a[j]
    if v>t:
        j-=1
    elif v<t:
        i+=1
    else:
        r+=1
        i+=1
print(r)