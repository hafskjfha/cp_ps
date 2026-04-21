import sys
I=lambda:sys.stdin.readline().strip()
for _ in range(int(I())):
    d=dict(x.split(':')for x in I().split(','))
    print(min(max(int(d[x])for x in p.split('&'))for p in I().split('|')))