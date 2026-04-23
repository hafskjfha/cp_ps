import sys

from itertools import combinations

input=sys.stdin.readline

T=int(input())

for _ in range(T):

	su=float("inf");	N=int(input())

	mbti=list(input().strip().split())

	if N>32:

		print(0)

	else:

		cbm=list(combinations(mbti,3))

		for a,b,c in cbm:

			ai=set(a)

			bi=set(b)

			ci=set(c)

			u=(len(ai-bi)+len(ai-ci)+len(ci-bi))

			su=min(su,u)

		print(su)