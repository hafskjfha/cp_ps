def main():
    import heapq
    input=open(0).readline
    pq=[]
    for d,w in sorted(tuple(map(int,input().split()))for _ in range(int(input()))):
        heapq.heappush(pq,w)
        if len(pq)>d:
            heapq.heappop(pq)
    print(sum(pq))
main()