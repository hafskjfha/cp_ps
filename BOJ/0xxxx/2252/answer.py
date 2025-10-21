def main():
    from collections import deque
    input=open(0).readline
    n,m=map(int,input().split())
    gr=[[]for _ in range(n+1)]
    in_nodes=[0]*(n+1)
    for _ in range(m):
        a,b=map(int,input().split())
        gr[a].append(b)
        in_nodes[b]+=1
    ans=[node for node in range(1,n+1)if in_nodes[node]==0]
    q=deque(ans)
    while q:
        node=q.popleft()
        for nnode in gr[node]:
            in_nodes[nnode]-=1
            if in_nodes[nnode]==0:
                q.append(nnode)
                ans.append(nnode)
    print(' '.join(map(str,ans)))
main()