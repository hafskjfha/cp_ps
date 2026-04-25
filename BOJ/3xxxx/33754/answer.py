from collections import deque

def solve():
    N = int(input())
    row1 = list(map(int, input().split()))
    row2 = list(map(int, input().split()))
    
    grid = [
        [0] + row1,  # 1-indexed
        [0] + row2
    ]

    visited = [[False] * (N + 1) for _ in range(2)]
    queue = deque()
    if grid[0][1] == 1:
        queue.append((0, 1))
        visited[0][1] = True

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 1 <= ny <= N:
                if grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    if not visited[1][N]:
        print(0)  # 도달 불가능
    elif all(grid[0][i] == 1 and grid[1][i] == 1 for i in range(1, N + 1)):
        print(2)  # 모든 칸이 1
    else:
        print(1)  # 일부 칸만 막힘

solve()
