com={}
for _ in range(int(input())):
    x=['red','yellow','green','brown','blue','pink','black'].index(input())+1
    com[x]=com.get(x,0)+1
i=1
ans=0
gc=False
while 1:
    if i&1:
        for k in range(7,1,-1):
            if com.get(k,0):
                ans+=k
                if com.get(1,0)==0:
                    com[k]-=1
                gc=True
                break
        else:
            gc=False
    else:
        if com.get(1,0):
            ans+=1
            com[1]-=1
        if not gc:
            break
    i+=1
print(ans)