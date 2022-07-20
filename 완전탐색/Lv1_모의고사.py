import sys
#1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
#2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
#3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

def solution(answers):
    #answer = []

    #babo1 = [1, 2, 3, 4, 5]
    #babo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    #babo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  

    ## 해당 길이만큼 들어오는 값을 나눈 나머지 idx를 찾으면 된다 !!!
    ## 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
    ## 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
    #babo1Len = len(babo1)
    #babo2Len = len(babo2)
    #babo3Len = len(babo3) 
    #babo1Cnt= 0
    #babo2Cnt=0 
    #babo3Cnt = 0
    
    #for i in range(len(answers)):
    #    if babo1[i%babo1Len] == answers[i]:
    #        babo1Cnt = babo1Cnt + 1
            
            
    #    if babo2[i%babo2Len] == answers[i]:
    #        babo2Cnt = babo2Cnt + 1
            
            
    #    if babo3[i%babo3Len] == answers[i]:
    #        babo3Cnt = babo3Cnt + 1
    
    #maxRank = max(babo1Cnt, babo2Cnt, babo3Cnt)
    #if maxRank == babo1Cnt:
    #    answer.append(1)
    #if maxRank == babo2Cnt:
    #    answer.append(2)
    #if maxRank == babo2Cnt:
    #    answer.append(3)
    #answer = sorted(answer)

    #return answer
    answer = []
    
    babo1 = [1, 2, 3, 4, 5]
    babo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    babo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]    
    
    babo1Len = len(babo1)
    babo2Len = len(babo2)
    babo3Len = len(babo3)
    
    babo1Cnt = 0
    babo2Cnt = 0
    babo3Cnt = 0
    
    
    for i in range(len(answers)):
        if babo1[i%babo1Len] == answers[i]:
            babo1Cnt = babo1Cnt + 1
            
            
        if babo2[i%babo2Len] == answers[i]:
            babo2Cnt = babo2Cnt + 1
            
            
        if babo3[i%babo3Len] == answers[i]:
            babo3Cnt = babo3Cnt + 1
            
            
    maxRank = max(babo1Cnt, babo1Cnt, babo3Cnt)
        
    if maxRank == babo1Cnt:
        answer.append(1)
    if maxRank == babo2Cnt:
        answer.append(2)
    if maxRank == babo3Cnt:
        answer.append(3)
    
    answer = sorted(answer)
    return answer



if __name__ == "__main__":
    answers = [1,3,2,4,2]
    print(solution(answers))