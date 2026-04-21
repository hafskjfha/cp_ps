input=open(0).readline
i=1
while 1:
    l=int(input())
    if l==0: break
    print(f'User {i}')
    for _ in range(int(input())):print(f'{l*int(input())/100000:.5f}')
    i+=1