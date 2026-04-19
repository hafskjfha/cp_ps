def main():
    input=open(0).readline
    L=[0]*10001
    for _ in range(int(input())):
        L[int(input())]+=1
    print=open(1,'w').write
    for i in range(1,10001):
        if L[i]!=0:
            for _ in range(L[i]):
                print(f'{i}\n')

main()