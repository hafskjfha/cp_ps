from itertools import permutations
n=int(input())
d=[input()for _ in " "*4]
for _ in range(n):
    s=input()
    for x in permutations(d,len(s)):
        for i in range(len(s)):
            if s[i]not in x[i]:
                break
        else:
            print('YES')
            break
    else:print('NO')