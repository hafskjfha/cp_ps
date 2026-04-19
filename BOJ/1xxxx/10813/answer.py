def main():
	input=open(0).readline
	n,m=map(int,input().split())
	a=[*range(1,n+1)]
	for _ in range(m):
		i,j=map(int,input().split())
		a[i-1],a[j-1]=a[j-1],a[i-1]
	print(*a)
main()