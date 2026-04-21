from collections import deque
N,K=map(int,input().split())
v=[0]*200001
def bfs():
	if K<N:
		return f'{N-K}\n1'
	q,a,m=deque([(N,0)]),0,float('inf')
	while q:
		x,d=q.popleft()
		if x==K:
			if d<=m:
				m=d
				a+=1
			continue
		for dx in (x-1,x+1,x*2):
			if 0<=dx<200001 and (v[dx]==0 or v[dx]==d+1) and d+1<m:
				q.append((dx,d+1))
				v[dx]=d+1
	return f'{m}\n{a}'
print(bfs())