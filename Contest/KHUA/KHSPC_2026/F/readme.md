# 문제 제목: [골프 연습](https://dojoi.xyz/ko/problems/180)
- **플랫폼**: DOJ
- **난이도**: 4.2/10
- **풀이 유형**: 그래프 / 0-1BFS 

---

## 1. 문제 요약
- 문제 핵심: 
  - $N \times M$격자판에서 골프를 쳐서 홀에 넣으려고 한다.
  - 상하좌우 중 원하는 방향으로 퍼팅을 할수 있다. 그런데 골프를 너무 잘쳐서 이동하는 경로에 벽이 없다면 원하는 만큼 한번에 직선으로 공을 이동시킬 수 있다.
  - 공을 홀에 넣기 위해 퍼팅을 해야하는 최솟값을 구하시오.
- 입력/출력 조건: 격자판에서 `#`은 벽, `.`은 빈칸, `S`는 초기 공의 위치, `T`는 홀의 위치이다. 어떤 방법으로도 공을 홀에 넣을 수 없다면 -1을 대신 출력한다.
- 제한 조건: $4 \le N,M \le 1000$, 격자의 테두리는 벽임이 보장된다.

---

## 2. 접근 아이디어
- 자력 풀이 시도:
  - 그냥 나이브 bfs로 돌면 $O(NM(N+M))$이기 떄문에 최적화를 해야한다.
  - 이전에 풀었던 [룩의 이동](/BOJ/3xxxx/34513/readme.md)을 생각해서 한칸에 4번만 방문되게 최적화해야 하는 것인가라고 생각했다.
- 막혔던 포인트:
  - 구현을 실수 한것일까 TLE를 받고 실패했다.
- 답지 참고 후:
  - 방향을 꺾지 않는 행동은 비용을 0로 생각하고 방향을 꺾는 행동은 비용을 1로 하여 생각한다면 0-1bfs로 문제를 해결할 수 있었다. (0-1bfs는 다익스트라로 환원 가능하므로 다익스트라도 가능하다.)
  - 마지막 퍼팅 방향을 차원으로 생각하여 거리 배열을 구성하고 업데이트 하면된다.

---

## 3. 코드 정리
[정답 코드](./answer.py)
```py
import sys
from collections import deque

def main():
    input=sys.stdin.readline
    n,m=map(int,input().split())
    board=[]
    start,end=None,None
    for i in range(n):
        s=input().strip()
        for j in range(m):
            if s[j]=='S':start=(i,j)
            elif s[j]=='T':end=(i,j)
        board.append(s)
    
    print(bfs(n,m,board,start,end))
    
    
def bfs(n,m,board,start,end):
    INF=float('inf')
    v=[[[INF]*4 for _ in range(m)] for _ in range(n)]
    delta=((0,1),(0,-1),(1,0),(-1,0))
    q=deque()
    
    for k,(dx,dy) in enumerate(delta):
        nx,ny=start[0]+dx,start[1]+dy
        if board[nx][ny]!='#':
            q.append((nx,ny,k))
            v[nx][ny][k]=1
    
    while q:
        x,y,d=q.popleft()
        
        if (x,y)==end: return v[x][y][d]
        
        for k, (dx,dy) in enumerate(delta):
            nx,ny=x+dx,y+dy
            
            if board[nx][ny]=='#': continue
            
            cost=v[x][y][d]+(d!=k)
            
            if cost < v[nx][ny][k]:
                v[nx][ny][k]=cost
                
                if d==k:
                    q.appendleft((nx,ny,k))
                else:
                    q.append((nx,ny,k))
                    
    
    return -1
    
main()
```

---

## 4. 시간/공간 복잡도

* 시간: $O(4NM)$
* 공간: $O(4NM)$

---

## 5. 배운 점 / 실수

* 어떤 행동을 하나의 간선으로 직접 표현하기 어렵더라도, 상태를 적절히 확장하고 비용을 0/1로 나누면 0-1 BFS로 해결할 수 있다.
