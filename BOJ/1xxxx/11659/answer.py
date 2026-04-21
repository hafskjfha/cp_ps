import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nu = list(map(int, input().split()))

# 누적 합 계산

cumulative_sum = [0] * (N + 1)

for i in range(1, N + 1):

    cumulative_sum[i] = cumulative_sum[i - 1] + nu[i - 1]

# 부분합 출력

for _ in range(M):

    i, j = map(int, input().split())

    print(cumulative_sum[j] - cumulative_sum[i - 1])

