n,m=map(int,input().split())
i=int
t=[0]*n
it=[0]*n
for _ in range(m):
    c,k,h,j=input().split()
    if k=='START':it[i(c)-1]=i(h)*60+i(j)
    else:t[i(c)-1]+=i(h)*60+i(j)-it[i(c)-1]
for x in t:print(x//60,x%60)