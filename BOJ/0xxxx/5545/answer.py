n=int(input())
a,b=map(int,input().split())
c=int(input())
d=sorted([int(input())for _ in range(n)],reverse=1)
ans=c//a
s=c
for i in range(n):
    s+=d[i]
    ans=max(ans,s//(b*(i+1)+a))
print(ans)