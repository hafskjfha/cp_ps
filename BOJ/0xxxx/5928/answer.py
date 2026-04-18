d,h,m=map(int,input().split())
a=(d-11)*1440+(h-11)*60+m-11
print([a,-1][a<0])