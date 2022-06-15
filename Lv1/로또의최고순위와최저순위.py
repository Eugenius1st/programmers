def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    zeroCnt = 0
    sameCnt = 0
    for i in lottos:
        if i == 0:
            zeroCnt+=1
    
    for x in win_nums:
        if x in lottos:
            sameCnt+=1
    answer = []
    answer.append(rank[sameCnt+zeroCnt])    
    answer.append(rank[sameCnt])

    return answer