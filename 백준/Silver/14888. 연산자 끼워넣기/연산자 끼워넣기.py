n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

minimum = 10**16
maximum = -(10**16)

def dfs(cur, plus, minus, mul, div, idx):
    global minimum
    global maximum
    if plus+minus+mul+div == 0:
        if cur<minimum:
            minimum = cur
        if cur>maximum:
            maximum = cur
        return
    if plus>0:
        dfs(cur+a[idx], plus-1, minus, mul, div, idx+1)
    if minus>0:
        dfs(cur - a[idx], plus, minus-1, mul, div, idx + 1)
    if mul>0:
        dfs(cur*a[idx], plus, minus, mul-1, div, idx + 1)
    if div>0:
        if cur<0:
            dfs(-(-cur//a[idx]), plus, minus, mul, div-1, idx+1)
        else:
            dfs(cur//a[idx], plus, minus, mul, div-1, idx+1)
dfs(a[0], b[0], b[1], b[2], b[3], 1)
print(maximum)
print(minimum)
