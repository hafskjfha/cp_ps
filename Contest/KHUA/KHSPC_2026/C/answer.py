def main():
    input=open(0).readline
    gs=input().split()
    t=[[],[],[],[]]
    s=input()
    for p in gs:
        for i in range(4):
            if p[i] not in t[i]: t[i].append(p[i])
    print(''.join(t[i][t[i][0]==s[i]] for i in range(4)))


main()