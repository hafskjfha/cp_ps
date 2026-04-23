a=sorted(filter(lambda x:x[1:3]==['jaehak','notyet']and not(0<int(x[3])<4),map(str.split,[*open(0)][1:])),key=lambda x:int(x[4]))[:10]
print(len(a))
print('\n'.join(sorted(x[0]for x in a)))