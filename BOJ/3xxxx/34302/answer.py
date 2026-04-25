ans=c=0
for _ in range(int(input())):
    s,t=map(int,input().split())
    if s>t:c+=1
    else:
        ans=max(ans,c)
        c=0
print(max(ans,c))