for a,b,c in map(str.split,[*open(0)][:-1]):
    a,c=int(a),int(c)
    print(['Not allowed'if a-c<-200 else a-c,a+c][b=='D'])