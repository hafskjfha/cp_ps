def main():
    input=open(0).readline
    n,m=map(int,input().split())
    gr=[[]for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,input().split())
        gr[u].append(v)
        gr[v].append(u)
    v,parent=bfs(gr,n)
    count=[0]*(n+1)
    dd=[0]*(n+1)
    srn=traceback(parent,n)
    for node in srn:
        c=v[node]
        count[c]=count[c]+1
        dd[c]=node
    for x in range(1,v[n]):
        if count[x]==1:
            return print(dd[x])
    print(1)

def bfs(gr,n):
    from collections import deque,defaultdict
    v=[-1]*(n+1)
    q=deque([(1,0)])
    parent=defaultdict(list)
    parent[1]=None
    v[1]=0
    while q:
        cur,d=q.popleft()
        for nxt in gr[cur]:
            if v[nxt]==-1:
                v[nxt]=d+1
                parent[nxt].append(cur)
                q.append((nxt,d+1))
            elif v[nxt]==d+1:
                parent[nxt].append(cur)
    return v,parent

def traceback(parent,n):
    from collections import deque
    short_route_nodes=[]
    q=deque([n])
    vv=[0]*(n+1)
    while q:
        x=q.popleft()
        if parent[x] is None: continue
        for nxt in parent[x]:
            if vv[nxt]==0:
                vv[nxt]=1
                q.append(nxt)
                short_route_nodes.append(nxt)
    return short_route_nodes
        
main()