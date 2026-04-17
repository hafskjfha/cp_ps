def main():
    from itertools import combinations
    for t in combinations(map(int,open(0)),7):
        if sum(t)==100: return print(*sorted(t))
main()