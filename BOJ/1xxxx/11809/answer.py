a,b=input(),input()
l=max(len(a),len(b))
a="0"*(l-len(a))+a
b="0"*(l-len(b))+b
aa,bb=[],[]
for i in range(l):
    x,y=a[i],b[i]
    if x==y:
        aa.append(x)
        bb.append(y)
    elif x>y:
        aa.append(x)
    else:
        bb.append(y)
for x in [aa,bb]:
    print(int("".join(x))if x else "YODA")