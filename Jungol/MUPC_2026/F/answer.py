from collections import deque
import sys

def main():
    input=sys.stdin.readline
    n=int(input())
    a=[*map(int,input().split())]
    
    ans=[None]*n
    dq=deque(range(n))
    
    x_max=0
    is_reversed=False
    a_index=0
    
    while dq:
        if is_reversed:
            index=dq.pop()
        else:
            index=dq.popleft()
        ans[index]=a[a_index]
        
        if a[a_index]>x_max:
            x_max=a[a_index]
            is_reversed = not is_reversed
        
        if dq:
            if is_reversed:
                dq.appendleft(dq.pop())
            else:
                dq.append(dq.popleft())
        
        
        a_index+=1
    
    print(' '.join(map(str,ans)))


main()