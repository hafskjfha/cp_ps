def main():
    from collections import deque
    n,l=map(int,input().split())
    a=[*map(int,input().split())]
    deq=deque()
    ans=[]

    for i in range(n):
        if deq and deq[0]<=i-l:
            deq.popleft()

        while deq and a[deq[-1]]>=a[i]:
            deq.pop()

        deq.append(i)

        ans.append(str(a[deq[0]]))

    print(' '.join(ans))

main()