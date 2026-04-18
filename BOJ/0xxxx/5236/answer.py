for _ in range(int(input())):
    s=input()
    temp=[s[-1]]
    ans=s[-1]
    for i in range(1,len(s)):
        temp.append(s[len(s)-i-1])
        for j in range(len(temp)-1):
            if temp[j]>temp[j+1]:break
        else:
            ans="".join(temp[::-1])
    print(f"The longest decreasing suffix of {s} is {ans}")