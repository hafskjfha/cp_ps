input=open(0).readline
n,b=map(int,input().split())
s=a=0
for x in sorted([int(input())for _ in range(n)],reverse=True):
    s+=x
    a+=1
    if s>=b:exit(print(a))