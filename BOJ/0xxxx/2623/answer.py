def main():
    from collections import deque
    input=open(0).readline
    n,m=map(int,input().split())
    gr=[[]for _ in range(n+1)]
    in_count=[0]*(n+1)
    for _ in range(m):
        k,*x=map(int,input().split())
        for i in range(k-1):
            node,next_node=x[i],x[i+1]
            gr[node].append(next_node)
            in_count[next_node]+=1
    result=[i for i in range(1,n+1)if in_count[i]==0]
    q=deque(result)
    while q:
        node=q.popleft()
        for next_node in gr[node]:
            in_count[next_node]-=1
            if in_count[next_node]==0:
                q.append(next_node)
                result.append(next_node)
    print([0,' '.join(map(str,result))][len(result)==n])
main()