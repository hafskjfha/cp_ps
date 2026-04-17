import math
gcd,lcm=map(int,input().split())
x=lcm//gcd
s=t=float('inf')
for a in range(1,int(x**0.5)+1):
    if x%a:continue
    b=x//a
    if math.gcd(a,b)==1 and s+t>a+b:s,t=a,b
print(s*gcd,t*gcd)