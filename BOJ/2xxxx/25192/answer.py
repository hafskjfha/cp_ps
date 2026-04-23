input=open(0).readline
ans=0
c=set()
for _ in range(int(input())):
    s=input().strip()
    if s=='ENTER':
        c.clear()
    else:
        if s not in c:
            ans+=1
            c.add(s)
print(ans)