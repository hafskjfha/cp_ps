for i in map(int,[*open(0)][:-1]):
	while i>9:
		print(i,end=' ')
		j=1
		for p in str(i):
			j*=int(p)
		i=j
	print(i)