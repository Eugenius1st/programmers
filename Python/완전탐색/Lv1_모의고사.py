def solution(answers):
    # 문제를 가장 많이 맞춘 사람이 누구인지! 
    # answer배열에 담아  return
    answer = []
    babo1 = [1,2,3,4,5] 
    babo2 = [2,1,2,3,2,4,2,5]
    babo3 = [3,3,1,1,2,2,4,4,5,5] 

    babo1Len = len(babo1) #.length
    babo2Len = len(babo2)
    babo3Len = len(babo3)

    babo1Score = 0
    babo2Score = 0
    babo3Score = 0

    for i in range(len(answers)):
        # 바보들이 답을 맞혔는지 확인
        if answers[i] == babo1[i%babo1Len]:
            babo1Score += 1
        if answers[i] == babo2[i%babo2Len]:
            babo2Score += 1
        if answers[i] == babo3[i%babo3Len]:
            babo3Score += 1
    rank = [babo1Score,babo2Score,babo3Score]
    
    # 가장 많이 맞춘 바보를 answer에 추가, 만약 중복있다면 sort
    temp = max(rank)                  # 같은 갯수의 문제를 맞췄으면 함께 출력
    for i in range(len(rank)):
        if rank[i] == temp:
            answer.append(i+1)
    return answer

