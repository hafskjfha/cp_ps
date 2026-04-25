from itertools import combinations
_,m=map(int,input().split())
s=a=0
for x in combinations(map(int,input().split()),3):
	if max(x)-min(x)>m:continue
	s+=1
	a=max(a,sum(x))
print(f"{s} {a}"if s else -1)