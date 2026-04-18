s=list(open(0).read())
for i in range(len(s)):
    if s[i]=='i':s[i]='e'
    elif s[i]=='e':s[i]='i'
    elif s[i]=='I':s[i]='E'
    elif s[i]=='E':s[i]='I'
print(''.join(s))