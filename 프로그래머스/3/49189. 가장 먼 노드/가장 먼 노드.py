from collections import deque
def solution(n, edge):
    answer = 0
    edges=[[] for _ in range(n+1)]
    
    for i in edge:
        edges[i[0]].append(i[1])
        edges[i[1]].append(i[0])
    
    q=deque()
    dist=[-1]*(n+1)
    q.append(1)
    cnt=0
    while q:
        now=q.popleft()
        if dist[now]==-1: 
            dist[now]=cnt
        
        for i in edges[now]:
            if dist[i]==-1:
                dist[i]=dist[now]+1
                q.append(i)
    maxdist=max(dist)
    for i in dist:
        if i==maxdist:
            answer+=1
        
        
    return answer