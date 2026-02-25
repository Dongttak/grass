def solution(k, dungeons):
    n=len(dungeons)
    visited=[False]*n #방문체크용
    def dfs(cur_k):
        best=0 #현재까지 최고기록 저장용 변수
        for i in range(n): #우리 저장되어있는 던전들 다 돌아보기
            if visited[i]:
                continue
            
            need, cost=dungeons[i]
            if cur_k>=need:
                visited[i]=True
                best=max(best, 1+dfs(cur_k-cost))
                visited[i]=False
        return best
    return dfs(k)
        
    
    