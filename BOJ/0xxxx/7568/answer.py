N = int(input())

people = []


for _ in range(N):

    weight, height = map(int, input().split())

    people.append((weight, height))



ranks = []

for person in people:

    rank = 1

    for other_person in people:

        if person[0] < other_person[0] and person[1] < other_person[1]:

            rank += 1

    ranks.append(rank)

# 덩치 등수를 출력합니다.

print(*ranks)

