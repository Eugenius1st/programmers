# 중요도가 높은 문서를 먼저 인쇄    
def solution(priorities, location):
    from collections import deque 
    document = deque()
    for x in range(len(priorities)):
        document.append((priorities[x],x))
    maxN = max(document)[0]
    answer = 0
    
    while True:
        tmp = document.popleft()
        if tmp[0] == maxN:
            answer+=1
            if tmp[1] == location:
                return answer
            maxN = max(document)[0]      

        else:
            document.append(tmp)  