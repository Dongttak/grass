from collections import Counter

def solution(str1, str2):
    answer = 0
    str1=str1.upper()
    set1=[]
    for i in range(1, len(str1)):
        if (str1[i]>='A' and str1[i]<='Z') and (str1[i-1]>='A' and str1[i-1]<='Z'):
            set1.append(str1[i-1:i+1])
    str2=str2.upper()
    set2=[]
    for i in range(1, len(str2)):
        if (str2[i]>='A' and str2[i]<='Z') and (str2[i-1]>='A' and str2[i-1]<='Z'):
            set2.append(str2[i-1:i+1])
    print(set1)
    print(set2)
    set3=Counter(set1) & Counter(set2)
    
    print(set3)
    length1=0
    for i in set3.values():
        length1+=i
    length2=0
    set4=Counter(set1) | Counter(set2)
    for i in set4.values():
        length2+=i
    if length2==0:
        return 65536
    else:
        answer=int(length1/length2*65536)
    return answer