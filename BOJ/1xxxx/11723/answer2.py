def main():
    import sys
    input=sys.stdin.readline
    r=[]
    s=0
    for _ in range(int(input())):
        c=input().split()
        cmd=c[0]

        if cmd=="add":
            s|=1<<(int(c[1])-1)
        elif cmd=="remove":
            s&=~(1<<(int(c[1])-1))
        elif cmd=="check":
            r.append(str((s>>(int(c[1])-1))&1))
        elif cmd=="toggle":
            s^=1<<(int(c[1])-1)
        elif cmd=="all":
            s=(1<<20)-1
        elif cmd=="empty":
            s=0
        if len(r)>100:
            print('\n'.join(r))
            r=[]
    print('\n'.join(r))
main()