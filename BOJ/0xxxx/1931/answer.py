import sys
input = sys.stdin.readline
N=int(input())
hl = []
for _ in range(N):
	hl.append(tuple(map(int,input().split())))
hl.sort(key=lambda x:(x[1],x[0]))

count = 0
end_time = 0

for meeting in hl:
    if meeting[0] >= end_time:
        count += 1
        end_time = meeting[1]

print(count)
