from collections import deque
N,K=map(int,input().split())
A=input().strip().split()
A1,A2,s,t=deque(),deque(),0,0
for i in range(N):
	if A[i]=='1':
		A1.append(i)
	else:
		A2.append(i)
while A1 and A2:
	if A1[0]<s+K and A2[0]<s+K:
		A1.popleft()
		A2.popleft()
		s+=2
	elif A1[0]<s+K:
		A1.popleft()
		s+=1
	else:
		A2.popleft()
		s+=1
	t+=1
print(t+len(A1)+len(A2))