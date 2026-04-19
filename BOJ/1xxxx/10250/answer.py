input=open(0).readline
for _ in range(int(input())):
	h,w,n=map(int,input().split())
	b=n%h
	c=n//h+1
	if not b:
		c-=1
		b=h
	print(f"{b}{c:02}")