input=open(0).readline
n,g=map(int,input().split())
k=[]
a=0
for _ in range(n):
    s,r=map(int,input().split())
    if s>r:a+=3
    else:k.append(r-s)
k.sort()
for x in k:
    if g-x>0:a+=3;g-=x+1
    elif x==g:a+=1;g-=x
    else:break
print(a)