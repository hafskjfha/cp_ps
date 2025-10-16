def main():
    import heapq
    input=open(0).readline
    n=int(input())
    pq=[]
    for d,w in sorted([tuple(map(int,input().split()))for _ in range(n)]):
        heapq.heappush(pq,w)
        if len(pq)>d:
            heapq.heappop(pq)
    print(sum(pq))
main()