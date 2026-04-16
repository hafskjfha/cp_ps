import sys

from collections import deque

input=sys.stdin.readline

N,M,V=map(int,input().split())

h=[]

graph=[[False]*(N+1) for _ in range(N+1)]

visited=[False]*(N+1)

for _ in range(M):

	a,b=map(int,input().split());	graph[a][b]=True

	graph[b][a]=True

def dfs(idx):

	global visited

	visited[idx]=True

	print(idx,end=" ")

	for n in range(1,N+1):

		if not visited[n] and graph[idx][n]:

			dfs(n)

dfs(V)

print()

def bfs():

	global q,visited

	while q:

		cur = q.popleft()

		print(cur,end=" ")

		for n in range(1,N+1):

			if not visited[n] and graph[cur][n]:

				visited[n] = True

				q.append(n)

				

visited=[False]*(N+1)

q=deque([V])

visited[V]=True

bfs()