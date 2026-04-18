p,q=map(int,input().split())
a=p+q
if a%2 or p-a//2<0:
    print(-1)
else:
    print(a//2,p-a//2)