from collections import deque
delta=((-1,0),(1,0),(0,-1),(0,1))
def main():
    input=open(0).readline
    n,m=map(int,input().split())
    mono=[]
    chesses_count=0
    chesses_coor=set()
    air=[[],[]]
    v=[[0]*m for _ in range(n)]
    cl_time=1
    for j in range(n):
        temp=input().split()
        mono.append(temp)
        for i in range(m):
            if temp[i]=='1': 
                chesses_count+=1
                chesses_coor.add((i,j))
    air[1]=s(n,m,mono,[(0,0)])
    
    while 1:
        uindex=cl_time&1
        up=set()
        for x,y in air[uindex]:
            is_cborder=False
            for dx,dy in delta:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and mono[ny][nx]=='1':
                    is_cborder=True
                    if v[ny][nx]==cl_time:
                        chesses_count-=1
                        air[1-uindex].append((nx,ny))
                        up.add((nx,ny))
                        if chesses_count==0:
                            print(cl_time)
                            return
                    v[ny][nx]=cl_time
            
            if is_cborder: air[1-uindex].append((x,y))
            for x,y in up:
                mono[y][x]='0'
        air[uindex]=[]
        air[1-uindex]=s(n,m,mono,air[1-uindex])
        cl_time+=1

def s(n,m,mono,start):
    coor=[]
    q=deque(start)
    v=[[0]*m for _ in range(n)]
    while q:
        x,y=q.popleft()
        for dx,dy in delta:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and mono[ny][nx]=='1':
                coor.append((x,y))
                break
        
        for dx,dy in delta:
            nx,ny=x+dx,y+dy
            if 0<=nx<m and 0<=ny<n and v[ny][nx]==0 and mono[ny][nx]=='0':
                q.append((nx,ny))
                v[ny][nx]=1
    return set(coor)
        
    
main()