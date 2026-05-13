MOD=998244353
a=b=c=0
for x in input():
    if x=='a':a+=(b+c+1)%MOD
    elif x=='b':b+=(a+c+1)%MOD
    else:c+=(a+b+1)%MOD
print((a+b+c)%MOD)