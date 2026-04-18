import sys
from collections import deque
input=sys.stdin.readline
def bfs(S):
	q,a,t,u=deque([S]),0,None,True
	while q:
		x,y=q.popleft()
		if o[y][x]==4:continue
		o[y][x]=4
		a+=1
		for dx,dy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if 0<=dx<N and 0<=dy<N and o[dy][dx]!=4:
				if o[dy][dx]==0:
					q.append((dx,dy))
					continue
				if not u:
					continue
				if o[dy][dx]==1 and t==None:
					t=1
				elif o[dy][dx]==2 and t==None:
					t=2
				elif t!=None and t==o[dy][dx]:
					pass
				elif t!=None and t!=o[dy][dx]:
					u,t=False,None
	if t==2:t=0
	return t,a	

while 1:
	try:
		N,B,W=map(int,input().split())
		o,b,w=[[0]*(N) for _ in range(N)],0,0
		t=[*map(int,input().split())]
		for i in range(0, B*2, 2):o[t[i+1]-1][t[i]-1]=1
		t=[*map(int,input().split())]
		for i in range(0, W*2, 2):o[t[i+1]-1][t[i]-1]=2
		for i in range(N):
			for j in range(N):
				if o[j][i]==0:
					e,c=bfs((i,j))
					if e==None:continue
					elif e:b+=c
					else:w+=c
		if b<w:print(f'White wins by {w-b}')
		elif b>w:print(f'Black wins by {b-w}')
		else:print('Draw')
	except:
		break