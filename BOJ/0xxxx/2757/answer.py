for s in map(str.strip,open(0)):
    if s=='R0C0':break
    r,c=s.split('C')
    col=[]
    c=int(c)
    while c>0:
        c-=1
        col.append(chr(ord('A')+(c%26)))
        c//=26
    print(''.join(col[::-1])+r[1:])