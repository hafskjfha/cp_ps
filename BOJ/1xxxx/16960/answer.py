n,m=map(int,input().split())
s=[set(input().split()[1:])for _ in range(n)]
print(+any(len(set().union(*(s[:i]+s[i+1:])))==m for i in range(n)))