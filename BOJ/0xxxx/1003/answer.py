def fibonacci(n, memo):

    if memo[n] != [-1, -1]:  # 이미 계산한 값이면 바로 반환

        return memo[n]

    if n == 0:

        memo[n] = [1, 0]  # 0은 한 번 출력됨

        return memo[n]

    elif n == 1:

        memo[n] = [0, 1]  # 1은 한 번 출력됨

        return memo[n]

    else:

        # 이전 호출에서 0과 1이 출력된 횟수를 가져와서 더해줌

        prev_0, prev_1 = fibonacci(n - 1, memo)

        prev_0, prev_1 = prev_0, prev_1

        curr_0, curr_1 = fibonacci(n - 2, memo)

        memo[n] = [prev_0 + curr_0, prev_1 + curr_1]

        return memo[n]

# 각 테스트 케이스마다 0과 1이 출력되는 횟수를 계산하여 출력

T = int(input())

for _ in range(T):

    N = int(input())

    memo = [[-1, -1] for _ in range(N + 1)]  # 메모이제이션 배열 초기화

    result = fibonacci(N, memo)

    print(result[0], result[1])

