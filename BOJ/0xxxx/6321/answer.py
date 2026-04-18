input=open(0).readline
for _ in range(int(input())):
	print(f"String #{_+1}")
	for i in input().strip():
		print("A" if i=="Z" else chr(ord(i)+1),end="")
	print("\n")