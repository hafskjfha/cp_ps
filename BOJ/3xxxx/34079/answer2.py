def main():
    input=open(0).readline
    n,m=map(int,input().split())
    gr=[[]for _ in range(n+1)]
    for _ in range(m):
        u,v=map(int,input().split())
        gr[u].append(v)
        gr[v].append(u)
    d1=bfs(1,gr,n)
    dn=bfs(n,gr,n)
    sh=d1[n]
    count=[0]*(sh+1)
    rr=[0]*(sh+1)
    for x in [x for x in range(1,n)if d1[x]+dn[x]==sh]:
        count[d1[x]]+=1
        rr[d1[x]]=x
    for i in range(1,sh):
        if count[i]==1:
            return print(rr[i])
    print(1)

def bfs(s,gr,n):
    from collections import deque
    v=[-1]*(n+1)
    q=deque([s])
    v[s]=0
    while q:
        cur=q.popleft()
        for nxt in gr[cur]:
            if v[nxt]==-1:
                v[nxt]=v[cur]+1
                q.append(nxt)
    return v
main()