import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

current_sum = sum(temp[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum += temp[i] - temp[i-K]
    max_sum = max(max_sum, current_sum)

print(max_sum)
