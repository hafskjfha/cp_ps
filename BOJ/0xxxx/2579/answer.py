import sys
input = sys.stdin.readline
N=int(input())
st = [0]
dp = [0] * (N+1)
for _ in range(N):
	st.append(int(input()))
if N==1:
	print(st[1])
elif N==2:
	print(sum(st[:3]))
else:
	dp[1] = st[1]
	dp[2] = st[1] + st[2]
	for i in range(3,N+1):
		dp[i] = max(dp[i-3]+st[i-1]+st[i], dp[i-2]+st[i])
	print(dp[-1])