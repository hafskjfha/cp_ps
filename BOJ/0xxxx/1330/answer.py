a,b=map(int,input().split())
s=["==","<"]
print(">"if a>b else s[a<b])