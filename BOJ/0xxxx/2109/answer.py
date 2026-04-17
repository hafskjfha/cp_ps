def main():
    import heapq
    input=open(0).readline
    pq=[]
    for w,d in sorted([tuple(map(int,input().split()))for _ in range(int(input()))],key=lambda x:x[1]):
        heapq.heappush(pq,w)
        if len(pq)>d:
            heapq.heappop(pq)
    print(sum(pq))
main()