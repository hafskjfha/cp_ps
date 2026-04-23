import sys,heapq
input=sys.stdin.readline
sell={}
def main():
	v=0
	for _ in range(int(input())):
		p,name,k,*c=input().strip().split()
		if p=="1":
			try:
				t=sell[name]
			except:
				sell[name]=[]
				t=[]
			for i in c:
				heapq.heappush(t,-int(i))
			sell[name]=t
		elif p=="2":
			try:
				for _ in range(int(k)):
					v+=(-(heapq.heappop(sell[name])))
			except:
				continue
	print(v)
main()