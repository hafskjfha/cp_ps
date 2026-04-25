a={i**2 for i in range(1,31700)}
print('\n'.join(["01"[n in a] for n in map(int,[*open(0)][1:])]))