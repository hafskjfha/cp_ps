import sys

input = sys.stdin.readline

N, K = map(int, input().split())

A = []

for _ in range(N):

    A.append(int(input()))

a = 0  # 필요한 동전의 최소 개수

while K > 0 and A:

    value = A.pop()  # 리스트의 끝에서부터 동전을 하나씩 꺼냄

    if K >= value:

        a += K // value  # 해당 동전을 사용할 수 있는 최대 횟수

        K %= value  # 남은 금액 업데이트

print(a)

