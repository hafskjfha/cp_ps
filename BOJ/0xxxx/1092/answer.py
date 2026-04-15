def main():
    from bisect import bisect_left
    n=int(input())
    cranes=sorted(map(int,input().split()))
    m=int(input())
    boxs=sorted(map(int,input().split()))
    ok_cranes=[[]for _ in range(n)]
    k=0
    if boxs[-1]>cranes[-1]:
        print(-1)
        return
    
    for box in boxs:
        if box<=cranes[k]:
            ok_cranes[k].append(box)
        else:
            k=bisect_left(cranes,box)
            ok_cranes[k].append(box)

    t=0
    while m:
        for i in range(n-1,-1,-1):
            for j in range(i,-1,-1):
                if ok_cranes[j]:
                    ok_cranes[j].pop()
                    m-=1
                    break
        t+=1
    print(t)
        

main()