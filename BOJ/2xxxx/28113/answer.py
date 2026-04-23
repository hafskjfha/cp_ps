n,a,b=map(int,input().split())
print(["Subway","Bus"][a<b]if a!=b else"Anything")