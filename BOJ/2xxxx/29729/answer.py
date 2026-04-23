def m():
    u=0
    s,_,_,*i=open(0).read().split()
    s=int(s)
    for c in i:
        u+=1if c=="1"else-1
        if s<u:s<<=1
    print(s)
m()