input=open(0).readline
for _ in range(int(input())):
    p='p'
    c=0
    for i in input().lower():
        if i==p:
            if i=='u':c+=1
            p='lup'['plu'.index(i)]
    print(c)