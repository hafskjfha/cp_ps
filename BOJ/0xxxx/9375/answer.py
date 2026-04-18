import sys

input=sys.stdin.readline

T = int(input())  

for _ in range(T):

    n = int(input())  

    clothes = {}  

    for _ in range(n):

        name, category = input().split()

        if category in clothes:

            clothes[category] += 1

        else:

            clothes[category] = 1

    

    result = 1

    for category in clothes:

        result *= (clothes[category] + 1)

    

    

    print(result - 1)

