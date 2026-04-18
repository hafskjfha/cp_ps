import sys

from collections import deque

input=sys.stdin.readline

def o(st):

	de=deque()	

	for c in st:

		if c =='(' or c=='[':

			de.append(c)

		elif c==')' or c==']':

			if c==')':

				if len(de)==0 or de[-1] !='(':

					return 'no'

				else:

					de.pop()

			elif c==']':

				if len(de)==0 or de[-1]!='[':

					return 'no'

				else:

					de.pop()

	if len(de)!=0:

		return 'no'

	else:

		return 'yes'

while True:

	S=input()

	if S=='.\n':

		break

	print(o(S))

			