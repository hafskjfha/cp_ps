for t in range(int(input())):
    _,s=input().split()
    c=0
    ans=0
    for i in range(len(s)):
        if s[i]=='0':continue
        if i<=c:
            c+=int(s[i])
        else:
            ans+=i-c
            c+=int(s[i])+i-c
    print(f"Case #{t+1}: {ans}")