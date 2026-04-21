for _ in range(int(input())):
	c={}
	for x in input():
		c[x]=c.get(x,0)+1
	for _ in range(int(input())):
		w=input()
		t={}
		for x in w:
			t[x]=t.get(x,0)+1
		for k,v in t.items():
			if c.get(k,0)<v:
				print("NO")
				break
		else: print("YES")