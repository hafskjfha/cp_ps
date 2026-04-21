import sys
sys.setrecursionlimit(10000)
n=int(input())
b=[*map(int,input().split())]
a=[]
ass=set()
def dfs(index):
    if len(a)==n:exit(print(*a))
        
    for x in range(1,n+1):
        if x not in ass and b[index]-a[-1]==x:
            ass.add(x)
            a.append(x)
            dfs(index+1)
            a.pop()
            ass.remove(x)

for x in range(1,n+1):
    ass.add(x)
    a.append(x)
    dfs(0)
    ass.remove(x)
    a.pop()