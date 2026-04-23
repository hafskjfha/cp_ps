def main():
    import sys
    input=sys.stdin.readline
    r=[]
    p=r.append
    S=[]
    for _ in range(int(input())):
    	o=input()
    	if o[0]=='1':S.append(o[2:-1])
    	elif o[0]=='2':p(S.pop()) if S else p(str(-1))
    	elif o[0]=='3':p(str(len(S)))
    	elif o[0]=='4':p('10'[len(S)>0])
    	else:p(S[-1]) if S else p(str(-1))
    sys.stdout.write('\n'.join(r))
main()