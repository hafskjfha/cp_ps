def floyd(n, gr):
	for i in range(n):
		for j in range(n):
			for k in range(n):
				gr[j][k]=min(gr[j][k],gr[j][i]+gr[i][k])