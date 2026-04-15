n,l=map(int,input().split())
for x in range(l,101):
    if 2*n%x==0:
        a=(2*n+x-x**2)//(2*x)
        if (2*n+x-x**2)%(2*x)==0 and a>-1:exit(print(*range(a,a+x)))
print(-1)