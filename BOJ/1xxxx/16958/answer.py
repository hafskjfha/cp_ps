import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

INF = float('inf')
N, T = map(int, input().rstrip().split())
total_nodes = []
teleport_nodes = []
node_values = []

for i in range(N):
    s, x, y = map(int, input().rstrip().split())
    total_nodes.append([x, y])
    if s:
        teleport_nodes.append([x, y])
for point in total_nodes:
    x1, y1 = point
    node_value = INF
    for teleportable_point in teleport_nodes:
        x2, y2 = teleportable_point
        distance = dist(x1, y1, x2, y2)
        if distance < node_value :
            node_value = distance
    node_values.append(node_value) 

M = int(input())
for _ in range(M):
    start, end = map(int, input().rstrip().split())
    x1, y1 = total_nodes[start-1]
    x2, y2 = total_nodes[end-1]
    print(min(dist(x1, y1, x2, y2), node_values[start-1] + T + node_values[end-1]))