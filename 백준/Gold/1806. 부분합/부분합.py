n, s=map(int, input().split())
a=list(map(int, input().split()))
start=0
current=0
answer=float('inf')

for end in range(n):
    current+=a[end]
    while current>=s:
        answer=min(answer, end-start+1)
        current-=a[start]
        start+=1

if answer==float('inf'):
    print(0)
else:
    print(answer)