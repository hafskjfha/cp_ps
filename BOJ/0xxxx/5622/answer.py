d=['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()

r=0
for i in word :
    for j in d :
        if i in j :
            r += d.index(j)+3
print(r)