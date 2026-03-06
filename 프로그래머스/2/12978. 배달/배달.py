import heapq
def solution(N, road, K):
    graph=[[] for _ in range(N+1)]
    
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    INF=float('inf')
    dist=[INF]*(N+1)
    dist[1]=0
    
    pq=[]
    heapq.heappush(pq, (0,1))
    
    while pq:
        cost, now=heapq.heappop(pq)
        
        if cost>dist[now]:
            continue
        for nxt, w in graph[now]:
            new_cost = cost + w
            
            if new_cost<dist[nxt]:
                dist[nxt]=new_cost
                heapq.heappush(pq, (new_cost,nxt))
                
    answer = 0
    for d in dist:
        if d <= K:
            answer += 1

    return answer