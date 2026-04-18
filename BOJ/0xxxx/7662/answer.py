import sys

import heapq

input = sys.stdin.readline  # input 함수를 sys.stdin.readline으로 대체

T = int(input().strip())  # 테스트 케이스 수, .strip()으로 개행 문자 제거

for _ in range(T):

    k = int(input().strip())  # 연산의 개수

    min_heap, max_heap = [], []

    visited = [False] * k  # 삭제된 원소를 표시하기 위한 배열

    for i in range(k):

        op, n = input().split()

        n = int(n)

        if op == 'I':

            heapq.heappush(min_heap, (n, i))

            heapq.heappush(max_heap, (-n, i))

            visited[i] = True

        elif op == 'D':

            if n == 1:  # 최댓값 삭제

                while max_heap and not visited[max_heap[0][1]]:

                    heapq.heappop(max_heap)

                if max_heap:

                    visited[max_heap[0][1]] = False

                    heapq.heappop(max_heap)

            else:  # 최솟값 삭제

                while min_heap and not visited[min_heap[0][1]]:

                    heapq.heappop(min_heap)

                if min_heap:

                    visited[min_heap[0][1]] = False

                    heapq.heappop(min_heap)

    # 최종 결과 확인 및 출력

    while min_heap and not visited[min_heap[0][1]]:

        heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:

        heapq.heappop(max_heap)

    if not min_heap or not max_heap:

        print("EMPTY")

    else:

        print(-max_heap[0][0], min_heap[0][0])

