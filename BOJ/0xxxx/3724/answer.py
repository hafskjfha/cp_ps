input=open(0).readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[[*map(int,input().split())]for _ in range(m)]
    ans=tm=float('-inf')
    for i in range(n):
        t=1
        for j in range(m):
            t*=a[j][i]
        if t>=tm:
            tm=t
            ans=i+1
    print(ans)