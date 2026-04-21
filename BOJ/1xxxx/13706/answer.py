def main():
	n=int(input())
	start,end=0,n
	while start<=end:
		mid=(start+end)//2
		k=pow(mid,2)
		if k==n:
			print(mid)
			return
		elif k<n:
			start=mid+1
		else:
			end=mid-1
main()