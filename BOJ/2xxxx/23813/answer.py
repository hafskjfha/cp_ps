s=input()
t=s
c=0
while 1:
    t=t[1:]+t[0]
    c+=int(t)
    if t==s:break
print(c)