def bfs(S,E):
    from collections import deque
    q,v=deque([(S,[])]),[False]*10001
    while q:
        x,l=q.popleft()
        if x==E:return l
        dx=x*2%10000
        if not v[dx]:
            q.append((dx,l+['D']))
            v[dx]=True
        dx=x-1
        if dx<0 and not v[9999]:
            q.append((9999,l+['S']))
            v[dx]=True
        elif dx>=0 and not v[dx]:
            q.append((dx,l+['S']))
            v[dx]=True
        dx=(x%1000)*10+x//1000
        if not v[dx]:
            q.append((dx,l+['L']))
            v[dx]=True
        dx=(x%10)*1000+x//10
        if not v[dx]:
            q.append((dx,l+['R']))
            v[dx]=True
def main():
    input=open(0).readline
    print=open(1,'w').write
    for _ in range(int(input())):
        print(''.join(bfs(*map(int,input().split()))));print('\n')

main()
            