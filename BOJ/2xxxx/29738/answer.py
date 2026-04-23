input=open(0).readline
for i in range(1,int(input())+1):
    k=int(input())
    if k<=25:print(f'Case #{i}: World Finals')
    elif k<=1000:print(f'Case #{i}: Round 3')
    elif k<=4500:print(f'Case #{i}: Round 2')
    else:print(f'Case #{i}: Round 1')