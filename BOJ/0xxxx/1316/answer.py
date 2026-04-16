s=0
for w in [*open(0)][1:]:
    k=set(w[0])
    for i in range(1,len(w.strip())):
        if w[i-1]!=w[i] and w[i] in k:
            break
        else:
            k.add(w[i])
    else:
        s+=1
print(s)