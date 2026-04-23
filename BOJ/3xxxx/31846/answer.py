I=open(0).readline
I()
s=I().strip()
for _ in range(int(I())):
    l,r=map(int,I().split())
    a=0
    for i in range(l,r):
        s1,s2=s[l-1:i][::-1],s[i:r]
        a=max(a,sum(s1[j]==s2[j]for j in range(min(len(s1),len(s2)))))
    print(a)