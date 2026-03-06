from collections import deque
def solution(n, results):
    answer = 0
    win=[[] for _ in range(n+1)]
    lose=[[] for _ in range(n+1)]
    for a, b in results:
        win[a].append(b)
        lose[b].append(a)
    def bfs(start, graph):
        visited=[False]*(n+1)
        q=deque()
        q.append(start)
        visited[start]=True
        cnt=0
        
        while q:
            now=q.popleft()
            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt]=True
                    q.append(nxt)
                    cnt+=1
        return cnt
    
    for i in range(1, n+1):
        if bfs(i, win)+bfs(i, lose) == n-1:
            answer+=1
            
    return answer