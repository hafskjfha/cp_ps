def main():
    input=open(0).readline
    for _ in range(int(input())):
        n,k=map(int,input().split())
        d=[*map(int,input().split())]
        graph=[[]for _ in range(n)]
        innode_count=[0]*n
        for _ in range(k):
            x,y=map(int,input().split())
            graph[x-1].append(y-1)
            innode_count[y-1]+=1
        w=int(input())

        build=sort(n,graph,innode_count)
        dp=d[:]
        for node in build:
            for next_node in graph[node]:
                dp[next_node]=max(dp[next_node],dp[node]+d[next_node])
        print(dp[w-1])

def sort(n,graph,innode_count):
    from collections import deque
    q=deque([node for node in range(n) if innode_count[node]==0])
    result=[]
    while q:
        node=q.popleft()
        result.append(node)
        for next_node in graph[node]:
            innode_count[next_node]-=1
            if innode_count[next_node]==0:
                q.append(next_node)
    return result

main()