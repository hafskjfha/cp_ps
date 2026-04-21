input=open(0).readline
for _ in range(int(input())):
    j,n=map(int,input().split())
    a=sorted([r*c for _ in range(n)for r,c in[map(int,input().split())]])
    c=0
    while j>0:
        j-=a.pop()
        c+=1
    print(c)
