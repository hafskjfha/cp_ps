n=int(input())
i=0
for _ in range(int(input())):
    m,x=map(int,input().split())
    i+=m*x
print("Yes" if n==i else "No")