from collections import deque
I=open(0).readline
r=[0,3,4,1,2]
n=int(I())
o=deque(map(int,I().split()))
s=set()
ans=[]
for _ in range(n):
    s.add(tuple(o))
    o.append(o.popleft())
for _ in range(int(I())):
    oo=[*map(int,I().split())]
    a,b=deque(),[]
    for x in oo:
        a.append(x)
        b.append(r[x])
    b=deque(b[::-1])
    for _ in range(n):
        if tuple(a) in s or tuple(b) in s:
            ans.append(oo)
            break
        a.append(a.popleft())
        b.append(b.popleft())
print(len(ans))
for x in ans:print(*x)