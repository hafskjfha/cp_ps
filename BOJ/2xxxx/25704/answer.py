n=int(input())
p=int(input())
a=[p]
if n>=5:
    a.append(p-500)
if n>=10:
    a.append(p-p*0.1)
if n>=15:
    a.append(p-2000)
if n>=20:
    a.append(p-p*0.25)
print(max(int(min(a)),0))