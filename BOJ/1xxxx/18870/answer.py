from bisect import bisect_left
import sys

input = sys.stdin.readline

N = int(input().strip())

X = list(map(int, input().split()))

coordinate = sorted(set(X))

ans = {}
r=[]
for i in range(N):
    r.append(str(bisect_left(coordinate, X[i])))
print(' '.join(r))
