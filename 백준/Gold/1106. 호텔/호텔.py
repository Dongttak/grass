import sys
input = sys.stdin.readline

c, n = map(int, input().split())
a = []
for _ in range(n):
    cost, customer = map(int, input().split())
    a.append((cost, customer))

INF = float('inf')
dp = [INF] * (c + 101)
dp[0] = 0

for cost, customer in a:
    for i in range(customer, c + 101):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[c:c+101]))