MOD=998244353
s=input()
ans=temp=0
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        n=i-temp
        ans=(ans+((n+1)*n)//2)%MOD
        temp=i
n=len(s)-temp
print((ans+((n+1)*n)//2)%MOD)