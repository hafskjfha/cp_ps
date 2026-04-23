a,b=map(int,input().split())
c,n=int(input()),int(input())
print(0if c<a else +(a*n+b<=c*n))