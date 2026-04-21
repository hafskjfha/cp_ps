psum=[0]
s=input()
ans=0
for x in s:
    psum.append(psum[-1]+int(x))
for i in range(len(s)):
    for j in range(i+2,len(s)+1,2):
        k=(i+j)//2
        if psum[j]-psum[k]==psum[k]-psum[i]:
            ans=max(ans,j-i)
print(ans)