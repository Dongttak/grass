from collections import deque

def solution(maps):
    n=len(maps) #y좌표
    m=len(maps[0]) #x좌표
    
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    q=deque()
    q.append((0,0,1))
    while q:
        nx,ny,cnt=q.popleft()
        for i in range(4):
            nxtx=nx+dx[i]
            nxty=ny+dy[i]
            if nxtx>=0 and nxtx<m and nxty>=0 and nxty<n and maps[nxty][nxtx]==1:
                maps[nxty][nxtx]=cnt+1
                q.append((nxtx, nxty, cnt+1))
    if maps[n-1][m-1]==1:
        return -1
    return maps[n-1][m-1]