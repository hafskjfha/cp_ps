print('Gnomes:')
for _ in range(int(input())):
    b=[*map(int,input().split())]
    print('UOnrodredreerde d'[sorted(b)==b or sorted(b,key=lambda x:-x)==b::2])