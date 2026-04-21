def check(s,i,j,f):
    while i<=j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            if f or (check(s,i+1,j,1)==2 and check(s,i,j-1,1)==2):return 2
            else:return 1
    return 0
for _ in range(int(input())):
    s=input()
    print(check(s,0,len(s)-1,0))