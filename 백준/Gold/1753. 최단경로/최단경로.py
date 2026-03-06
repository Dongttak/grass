import heapq
import sys
input=sys.stdin.readline
v,e=map(int, input().split())
s=int(input())
a=[]

graph=[[] for _ in range(v+1)]

for i in range(e):
    p,q,r=map(int,input().split())
    graph[p].append((q,r))

INF=float('inf')

pq=[]
dist=[INF]*(v+1)
dist[s]=0
heapq.heappush(pq, (0, s))
while pq:
    cost, now=heapq.heappop(pq)
    
    if cost > dist[now]:
        continue
    
    for nxt, w in graph[now]:
        new_cost=cost+w
        if dist[nxt]>new_cost:
            dist[nxt]=new_cost
            heapq.heappush(pq, (new_cost, nxt))
            
for i in range(1, v+1):
    if dist[i]==float('inf'):
        print("INF")
    else:
        print(dist[i])
