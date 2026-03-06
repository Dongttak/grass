import itertools
n, m=map(int, input().split())

a=[]
for i in range(n):
    a.append(list(map(int, input().split())))
chicken=[]
home=[]
for i in range(n):
    for j in range(n):
        if a[i][j]==2:
            chicken.append([i, j])
        elif a[i][j]==1:
            home.append([i,j])


minimum=float('inf')

for i in itertools.combinations(chicken, m):
    total=0
    
    for j in home:
        mini=float('inf')
        for k in i:
            dist=abs(k[0]-j[0])+abs(k[1]-j[1])
            mini=min(mini, dist)
        total+=mini
    minimum=min(minimum, total)
print(minimum)
