for _ in range(int(input())):
    s=input()
    ans=[s[0]]
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:ans.append(s[i])
    print("".join(ans))