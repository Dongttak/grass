def solution(a):
    n=len(a)
    
    left=[0]*n
    right=[0]*n
    
    left[0]=a[0]
    for i in range(1,n):
        left[i]=min(left[i-1], a[i])
        
    right[n-1]=a[n-1]
    for i in range(n-2,-1,-1):
        right[i]=min(right[i+1], a[i])
    
    answer=0
    for i in range(n):
        if not (a[i]>left[i] and a[i]>right[i]):
            answer+=1
            
    return answer