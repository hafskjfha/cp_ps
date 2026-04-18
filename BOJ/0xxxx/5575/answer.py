for s in map(str.split,open(0)):
    h1,m1,s1,h2,m2,s2=map(int,s)
    d=(h2-h1)*3600+(m2-m1)*60+s2-s1
    print(d//3600,d%3600//60,d%60)