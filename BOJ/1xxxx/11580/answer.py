input()
c=input()
a=set([(0,0)])
x,y=0,0
for n in c:
    if n=="E":
        x+=1
        a.add((x,y))
    elif n=="W":
        x-=1
        a.add((x,y))
    elif n=="S":
        y-=1
        a.add((x,y))
    else:
        y+=1
        a.add((x,y))
print(len(a))