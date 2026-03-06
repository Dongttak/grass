import itertools 
def solution(numbers): 
    answer=set() 
    numbers.sort() 
    tool=list(itertools.permutations(numbers, 2)) 
    for i in tool: 
        answer.add(sum(i)) 
    answer=sorted(answer) 
    return answer