def main():
    import os
    input=os.read(0,os.stat(0).st_size).decode().splitlines().__iter__().__next__
    l,n,k=map(int,input().split())
    a=[*map(int,input().split())]
    from collections import deque
    q=deque([(x,0)for x in a])
    v=set(a)
    r=['0']*min(k,n)
    c=min(k,n)
    while q and c<k:
        x,d=q.popleft()
        if 0<=x-1 and x-1 not in v:
            q.append((x-1,d+1))
            v.add(x-1)
            r.append(f"{d+1}")
            c+=1
            if c>=k:break
        if x+1<=l and x+1 not in v:
            q.append((x+1,d+1))
            v.add(x+1)
            r.append(f"{d+1}")
            c+=1
            if c>=k:break
    encode=str.encode
    os.write(1,b'\n'.join(map(encode,r)))
    os._exit(0)
            

main()