import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

size = [0] * (n+1)

def dfs(cur, parent):
    size[cur] = 1
    for nxt in graph[cur]:
        if nxt == parent:
            continue
        size[cur] += dfs(nxt, cur)
    return size[cur]

dfs(r, 0)
for i in range(q):
    temp=int(input())
    print(size[temp])