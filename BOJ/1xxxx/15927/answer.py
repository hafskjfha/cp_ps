s=input()
print(-1if len(set(s))==1 else len(s)-(s==s[::-1]))