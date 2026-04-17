import re
print('\n'.join(map(str,sorted(map(int,[i for s in map(lambda x:re.findall(r'\d+', x),[*open(0)][1:]) for i in s])))))
