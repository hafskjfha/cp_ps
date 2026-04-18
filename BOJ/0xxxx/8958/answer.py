import string,sys

input=sys.stdin.readline

T=int(input())

for _ in range(T):

	S=input().strip();	so=0

	bs=0

	for a in list(S):

		if a=="O":

			bs+=1

			so+=bs

		else:

			bs=0

	print(so)