input=open(0).readline
for _ in range(int(input())):
    n=int(input())
    k=1
    a=0
    while n//5**k:
        a+=n//5**k
        k+=1
    print(a)