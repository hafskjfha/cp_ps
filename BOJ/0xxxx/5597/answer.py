import sys
input=sys.stdin.readline
h=set()
r=set(range(1,31))
for _ in range(28):
	h.add(int(input()))
print('\n'.join(map(str,sorted(r-h))))