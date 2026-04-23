f=lambda n:''.join('딸기'if int(b)else'V'for b in f'{n:04b}')
s=[f(n)for n in[*range(1,16),*range(14,0,-1)]]
for n in map(int,[*open(0)][1:]):
    print(s[(n-1)%28])
