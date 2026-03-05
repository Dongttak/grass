from collections import deque
def solution(maps):
    cand=[]
    n=len(maps) #y
    m=len(maps[0]) #x
    print(m, n)
    
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    visited=[[False]*m for _ in range(n)]
    visited[0][0]=True
    
    q=deque()
    q.append((0,0,1))
    while q:
        y,x,c=q.popleft()
        if y==n-1 and x==m-1:
            cand.append(c)
            
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<m and ny>=0 and ny<n and not visited[ny][nx] and maps[ny][nx]!=0:
                q.append((ny,nx,c+1))
                visited[ny][nx]=True
                
    if cand:
        return min(cand)
    return -1