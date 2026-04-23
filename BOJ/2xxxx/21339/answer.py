n,k=map(int,input().split())
d,s=map(int,input().split())
a=(n*d-k*s)/(n-k)
print(a if 0<=a<=100 else'impossible')