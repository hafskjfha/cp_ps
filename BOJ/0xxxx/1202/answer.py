def main():
    import heapq,sys
    push=heapq.heappush
    pop=heapq.heappop
    input=sys.stdin.readline
    n,k=map(int,input().split())
    gems=sorted(tuple(map(int,input().split()))for _ in range(n))
    bags=sorted(int(input())for _ in range(k))
    pq=[]
    gem_index=0
    ans=0
    for bag in bags:
        while gem_index<n and gems[gem_index][0]<=bag:
            m,v=gems[gem_index]
            push(pq,-v)
            gem_index+=1
        if pq:
            ans+=-pop(pq)
    print(ans)

main()