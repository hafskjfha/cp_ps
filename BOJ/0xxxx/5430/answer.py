import sys

from collections import deque

import json

input=sys.stdin.readline

T=int(input())

def D(deq,r):

	if r==0:		deq.popleft()

	else:

		deq.pop()

	return deq

for _ in range(T):

	p=list(input().strip())

	l=int(input())

	a=input().strip()

	aa=json.loads(a)

	de=deque(aa)

	r=0

	e=False

	for f in p:

			if f=='R':

				if r==0:

					r=1

				else:

					r=0

			elif f=='D':

				if len(de)==0:

					print("error")

					e=True

					break

				else:

					de=D(de,r)

					

	if not e:

		if r:

			de.reverse()

		print("["+",".join(map(str,de))+"]")