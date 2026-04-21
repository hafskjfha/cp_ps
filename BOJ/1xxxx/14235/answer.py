import heapq
pq=[]
input=open(0).readline
for _ in range(int(input())):
    i,*a=map(int,input().split())
    if i==0:print(-heapq.heappop(pq)if pq else -1)
    else:
        for y in a:heapq.heappush(pq,-y)