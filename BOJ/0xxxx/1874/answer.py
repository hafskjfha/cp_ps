from collections import deque
import sys

n = int(input())  # n 입력 받기
sequence = [int(sys.stdin.readline().strip()) for _ in range(n)]  # 수열 입력 받기

stack = deque()  # deque로 스택 초기화
result = []  # 연산 결과 저장 리스트
current = 1  # 현재 push 해야 할 숫자

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    for op in result:
        print(op)
