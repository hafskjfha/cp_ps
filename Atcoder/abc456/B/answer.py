d1=[*map(int,input().split())]
d2=[*map(int,input().split())]
d3=[*map(int,input().split())]
ans=0
for x,y,z in ((4,5,6),(4,6,5),(5,4,6),(5,6,4),(6,4,5),(6,5,4)):
    t=1
    t*=d1.count(x)/6
    t*=d2.count(y)/6
    t*=d3.count(z)/6
    ans+=t
print(ans)