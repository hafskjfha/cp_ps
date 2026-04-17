import heapq,sys
input=sys.stdin.readline
heap=[]
N=int(input())
A=0
for _ in range(N):
    L=[*map(int,input().split())]
    for i in L:
        if A<N:
            heapq.heappush(heap,i)
            A+=1
        else:
            if heap[0]<i:
                heapq.heappop(heap)
                heapq.heappush(heap,i)
print(heapq.heappop(heap))