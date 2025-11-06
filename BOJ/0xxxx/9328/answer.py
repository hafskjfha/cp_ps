from collections import deque,defaultdict
delta=((-1,0),(1,0),(0,-1),(0,1))
def main():
    input=open(0).readline
    for _ in range(int(input())):
        n,m=map(int,input().split())
        board=[input().strip()for _ in range(n)]
        temp=input().strip()
        keys=set(temp)if temp!='0'else set()
        print(solve(n,m,board,keys))

def solve(n,m,board,keys):
    starts=[]
    v=[[0]*m for _ in range(n)]
    doors=defaultdict(list)
    ans=0
    for i in range(m):
        ans=ss(i,0,board,starts,v,ans,keys,doors)
        ans=ss(i,n-1,board,starts,v,ans,keys,doors)
    for i in range(1,n-1):
        ans=ss(0,i,board,starts,v,ans,keys,doors)
        ans=ss(m-1,i,board,starts,v,ans,keys,doors)
    if not starts: return 0
    return bfs(n,m,board,keys,starts,v,ans,doors)
    
def bfs(n,m,board,keys,starts,v,ans,doors):
    q=deque(starts)
    while q:
        x,y=q.popleft()
        for dx,dy in delta:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and board[ny][nx]!='*' and v[ny][nx]==0:
                c=board[ny][nx]
                v[ny][nx]=1
                if c=='$':
                    ans+=1
                    q.append((nx,ny))
                elif c=='.': q.append((nx,ny))
                elif 65<=ord(c)<=90:
                    if c.lower() in keys: q.append((nx,ny))
                    else: doors[c.lower()].append((nx,ny))
                elif 97<=ord(c)<=122:
                    q.append((nx,ny))
                    if c not in keys:
                        keys.add(c)
                        [q.append((dox,doy))for dox,doy in doors[c]]

    return ans

def ss(x,y,board,starts,v,ans,keys,doors):
    c=board[y][x]
    if c=='*': return ans
    elif c=='$':
        starts.append((x,y))
        v[y][x]=1
        return ans+1
    elif c=='.':
        starts.append((x,y))
        v[y][x]=1
    elif 65<=ord(c)<=90:
        if c.lower() in keys:
            starts.append((x,y))
        else:
            doors[c.lower()].append((x,y))
        v[y][x]=1
    elif 97<=ord(c)<=122:
        starts.append((x,y))
        keys.add(c)
        v[y][x]=1
        if doors[c.upper()]: starts.extend(doors[c.upper()])
    return ans
main()