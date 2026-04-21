I=open(0).readline
n=int(I())
a=[]
b=[]
c=0
ans=0
for _ in range(n):
    x,y=map(int,I().split())
    if x<=y:a.append((x,y))
    else:b.append((x,y))
a.sort()
b.sort(key=lambda x:(-x[1],-x[0]))
for x,y in a+b:
    if x>c:ans+=x-c;c=x
    c+=y-x
print(ans)