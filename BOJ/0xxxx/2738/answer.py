n,m=map(int,input().split())
a=[[*map(int,input().split())]for _ in range(n)]
b=[[*map(int,input().split())]for _ in range(n)]
[print(*[a[i][j]+b[i][j]for j in range(m)])for i in range(n)]