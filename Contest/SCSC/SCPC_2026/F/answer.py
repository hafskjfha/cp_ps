from collections import deque

def main():
    input=open(0).readline
    q=int(input())
    x=[*map(int,input().split())]
    t=[]
    C=None
    ans=[C]*q
    gr=[[]for _ in range(q)]
    for i in range(q):
        y=x[i]
        if y<0:
            ans[i]=str(x[-y-1])
        else:
            gr[y-1].append(i) # bfs로 전파를 위해 간선의 방향을 뒤집음
    dq=deque(i for i in range(q) if ans[i]!=C)
    #print(dq)
    while dq:
        x=dq.popleft()
        for y in gr[x]:
            ans[y]=ans[x]
            dq.append(y)
        
    print(' '.join([[x,str(q)][x==C] for x in ans]))

main()