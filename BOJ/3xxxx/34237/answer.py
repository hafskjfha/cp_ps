input=open(0).readline
buffer=[]
n,m=map(int,input().split())
k=[tuple(map(int,input().split())) for _ in range(n)]
for _ in range(m):
    g,x,y=map(int,input().split())
    ans=0
    for a,b in k:
        if x<=a and y<=b and a+b<=g:
            ans+=1
    buffer.append(str(ans))
print('\n'.join(buffer))