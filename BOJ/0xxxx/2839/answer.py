import sys

input=sys.stdin.readline

N = int(input())

def op(k):

	m = 0	

	m += k//5

	

	w = k%5

	if w ==0:

		return m

	while w:

		if w%3 ==0:

			m += w//3

			return m

		else:

			if m != 0:

				m -= 1

				w += 5

			else:

				return -1

print(op(N))