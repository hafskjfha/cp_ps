from collections import deque
def main():
    input=open(0).readline
    for _ in range(int(input())):
        n,m=map(int,input().split())
        gr=[[i]for i in range(n)]
        for _ in range(m):
            u,v=map(int,input().split())
            gr[u-1].append(v-1)
            gr[v-1].append(u-1)
        w=int(input())
        h=[input().strip()for _ in range(n)]
        print("NYoe s"[solve(n,m,gr,w,h)::2])

def solve(n,m,gr,w,h):
    gr2={}
    ind={}
    for u in range(n):
        for v in gr[u]:
            for i in range(w):
                if h[u][i]=='o' and h[v][(i+1)%w]=='o':
                    gr2.setdefault((u,i),[]).append((v,(i+1)%w))
                    ind[(u,i)]=0
                    ind[(v,(i+1)%w)]=0


    
    for x in gr2.values():
        for t in x:ind[t]+=1
    q=deque(k for k,v in ind.items()if v==0)
    c=0
    while q:
        t=q.popleft()
        c+=1
        for k in gr2.get(t,[]):
            ind[k]-=1
            if ind[k]==0:
                q.append(k)
                
    return any(ind.values())

main()