i=map(int,open(0)).__next__
for _ in range(i()):
    g=i()
    n=[i()for _ in range(g)]
    for m in range(1,10**6-1):
        if len(set(j%m for j in n))==g:
            print(m)
            break