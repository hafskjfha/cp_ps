input=open(0).readline
s1=list(input().strip())
s2=[]
for _ in range(int(input())):
    c,*x=input().split()
    if c=='L':
        if s1:s2.append(s1.pop())
    elif c=='D':
        if s2:s1.append(s2.pop())
    elif c=='B':
        if s1:s1.pop()
    else:
        s1.append(x[0])
print("".join(s1),"".join(s2[::-1]),sep="")