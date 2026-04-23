k,*l=open(0).read().splitlines()
d={}
for x in l[::-1]:d[x]=d.get(x,0)-1
print('\n'.join(sorted(d,key=d.get)[:int(k.split()[1])]))