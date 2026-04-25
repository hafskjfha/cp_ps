n,m,a,b=map(int,input().split())
c=n*3-m
print(a*c+b if c>0 else 0)