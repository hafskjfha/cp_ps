from collections import deque
input=open(0).readline
n=int(input())
q=deque()
while 1:
    x=input().strip()
    if x=="-1":exit(print(" ".join(q)or"empty"))
    elif x=="0":q.popleft()
    else:
        if len(q)<n:q.append(x)