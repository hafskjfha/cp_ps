import sys
sys.setrecursionlimit(10**5)
ans=0
del_node=None
def dfs(node,gr,v):
    global ans,del_node
    is_leaf=True
    for nnode in gr[node]:
        if nnode!=del_node:
            is_leaf=False
            if v[nnode]!=1:
                v[nnode]=1
                dfs(nnode,gr,v)
            
    if is_leaf:
        ans+=1

def main():
    global del_node,ans
    n=int(input())
    gr=[[]for _ in range(n)]
    a=[*map(int,input().split())]
    root=None
    for i in range(n):
        if a[i]==-1:
            root=i
            continue
        gr[a[i]].append(i)
    del_node=int(input())
    if del_node==root:
        return print(0)
    dfs(root,gr,[0]*n)
    print(ans)
main()