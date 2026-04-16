from collections import deque
N,K=map(int,input().split())
v=set()
def bfs():
	q=deque([(N,0)])
	while q:
		x,d=q.popleft()
		if x in v:continue
		if x==K:return d
		v.add(x)
		for dx in (x-1,x+1,x*2):
			if 0<=dx<100001 and dx not in v:
				q.append((dx,d+1))
print(bfs())