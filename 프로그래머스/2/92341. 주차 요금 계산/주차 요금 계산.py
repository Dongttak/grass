from collections import deque

def solution(fees, records):
    answer = []
    car=[]
    for i in records:
        name=""
        for j in range(4):
            name+=i[6+j]
        if [name,0] not in car:
            car.append([name, 0])
    length=len(records)
    for i in car:
        queue=deque()
        for j in records:
            name=""
            for k in range(4):
                name+=j[6+k]
            if i[0]==name and j[11:]=="IN":
                hour=int(j[:2])
                minute=int(j[3:5])
                queue.append(hour*60+minute)
            elif i[0]==name and j[11:]=="OUT":
                hour=int(j[:2])
                minute=int(j[3:5])
                time=hour*60+minute
                i[1]+=time-queue.popleft()
        if queue:
            i[1]+=(23*60+59)-queue.popleft()
    
    car.sort(key=lambda x:x[0])
    print(car)
    for i in car:
        if i[1]<=fees[0]:
            answer.append(fees[1])
        else:
            i[1]-=fees[0]
            if i[1]%fees[2]==0:
                answer.append(fees[1]+(i[1]//fees[2])*fees[3])
            else:
                answer.append(fees[1]+(i[1]//fees[2]+1)*fees[3])
    
    return answer