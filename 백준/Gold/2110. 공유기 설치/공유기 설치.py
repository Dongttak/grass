n,m=map(int, input().split())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
low=1
high=a[-1]-a[0]
ans=0
def search(d):
    cnt=1
    last = a[0]
    for i in a[1:]:
        if i-last>=d:
            cnt+=1
            last = i
            if cnt>=m:
                return True
    return False

while low<=high:
    mid=(low+high)//2
    if search(mid):
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(ans)
