n=int(input())
w=600
a=0
for x,y in sorted(((x%100+x//100*60-10),(y%100+y//100*60+10))for _ in range(n)for x,y in[map(int,input().split())]):
    a=max(a,x-w)
    w=max(w,y)
print(max(a,1320-w))