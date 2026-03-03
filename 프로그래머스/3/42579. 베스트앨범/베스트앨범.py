def solution(genres, plays):
    answer = []
    a=[]
    length=len(genres)
    for i in range(length):
        if [genres[i], 0] not in a:
            a.append([genres[i], 0])
    for i in a:
        for j in range(length):
            if i[0]==genres[j]:
                i[1]+=plays[j]
    a.sort(key=lambda x:x[1], reverse=True)
    
    for i in a:
        b=[]
        for j in range(length):
            if i[0]==genres[j]:
                b.append([plays[j], j])
        b.sort(key=lambda x:x[0],reverse=True)
        if len(b)==1:
            answer.append(b[0][1])
        else:
            for j in range(2):
                answer.append(b[j][1])
        
        
            
    
    return answer