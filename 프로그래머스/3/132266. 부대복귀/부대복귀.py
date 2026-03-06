from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    graph=[[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append(b)
        graph[b].append(a)
    def bfs(start):
        visited=[-1]*(n+1)
        q=deque()
        q.append(start)
        visited[start]=0
        while q:
            now=q.popleft()
            for i in graph[now]:
                if visited[i]==-1:
                    visited[i]=visited[now]+1
                    q.append(i)
        return visited
    
    t=bfs(destination)
    for i in sources:
        answer.append(t[i])
    return answer