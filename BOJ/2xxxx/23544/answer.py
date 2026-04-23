n=int(input())
print(n-len({input()for _ in range(n)}))