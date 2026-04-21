import sys

def ssss(nu):

	if nu-int(nu) >= 0.5:		return int(nu)+1

	else:	return int(nu)

J = int(sys.stdin.readline())
N=[]
for i in range(J):
    N.append(int(sys.stdin.readline().strip()))


if J == 0:

	print(0)

else:

	gd = ssss(J*0.15)

	if gd >0 : 

		N = sorted(N)[gd:-gd]

		qj = sum(N)/len(N)

		qr = ssss(qj)

	else:
		
		k = sum(N)/len(N)

		qr=ssss(k)
		
        

	print(qr)