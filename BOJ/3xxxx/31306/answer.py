s=input()
a=sum([s.count(p)for p in "aeiou"])
print(a,a+s.count('y'))