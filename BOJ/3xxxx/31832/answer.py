import re
for _ in range(int(input())):
    s=input()
    a=0
    for c in re.sub('[^a-zA-Z]','',s):a+=1if 97<=ord(c)<=122else-1
    if re.search(r'\D',s)and len(s)<11 and a>=0:print(s)