def main():
    from collections import deque
    input = open(0).readline
    N, M = map(int, input().split())
    G:list[tuple[int,int]|None] = [None]*(N+1)
    A:dict[int,int] = {}
    S = [1]*(N+1)
    for i in range(N):
        x,y = map(int, input().split())
        G[i+1]=(x,y)
    P = [*map(int, input().split())]
    R = [*map(int, input().split())]
    R0 = R[0]**2
    for i in range(M):
        A[P[i]]=max(R[i+1]**2,A.get(P[i],0))
        S[P[i]]=0
    for k,v in A.items():
        Xi,Yi = G[k]
        for j in range(1,N+1):
            if k==j:continue
            Xj,Yj = G[j]
            if (Xi-Xj)**2+(Yi-Yj)**2<=v:
                S[j]=0
    
    q = deque([i for i in range(1,N+1) if S[i]])
    V = [0]*(N+1)
    while q:
        b = q.popleft()
        Xi,Yi = G[b]
        for j in range(1,N+1):
            Xj,Yj=G[j]
            if V[j]:continue
            if (Xi-Xj)**2+(Yi-Yj)**2<=R0:
                V[j]=1
                q.append(j)
                S[j]=1
    print(sum(S)-1)
main()