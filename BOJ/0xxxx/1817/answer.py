N,M=map(int,input().split())
if N:
	g=0
	b=1
	for i in [*map(int,input().split())]:
		if g+i<=M:
			g+=i
		else:
			b+=1
			g=i
	print(b)
else:
	print(0)