
import sys
input=sys.stdin.readline

import heapq

n, m=map(int, input().split())
con=[]

graph=[[] for _ in range(n+1)]
indegree=[0]*(n+1)

for _ in range(m):
    a, b=map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(con, i)

answer = []

while con:
    cur = heapq.heappop(con)
    answer.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(con, nxt)

print(*answer)
