def solution(k, dungeons):
    best=0
    n=len(dungeons)
    visited=[False]*n
    
    def dfs(k, cnt):
        nonlocal best
        best=max(cnt, best)
        
        for i in range(n):
            need, cost=dungeons[i]
            if not visited[i] and k>=need:
                visited[i]=True
                dfs(k-cost, cnt+1)
                visited[i]=False
    dfs(k, 0)
    return best