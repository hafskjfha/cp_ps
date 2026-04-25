def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    c = int(input())
    fish = [tuple(map(int, input().split())) for _ in range(n)]

    fish.sort(key=lambda x: -x[1])

    max_x_sum = sum(x for x, _, _ in fish)
    ans = 0

    for T in range(max_x_sum + 1):
        t = T
        profit = 0

        for x, s, w in fish:
            if x <= t:
                t -= x
                profit += w

        ans = max(ans, profit - T * c)

    print(ans)
main()