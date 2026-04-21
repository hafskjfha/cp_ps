def main():
    from itertools import combinations
    import sys
    input=sys.stdin.readline
    n,m=map(int,input().split())
    p=[[*map(int,input().split())]for _ in range(n)]
    ans=0
    for combo in combinations([*range(m)], 3):
        ans=max(ans,sum([max([p[i][j]for j in combo]) for i in range(n)]))
    print(ans)
main()