import sys
input = sys.stdin.readline
while True:
    li = input()
    if li == "":
        break
    li = li.strip()
    l = map(int,li.split())
    print(sum(l))
    
    