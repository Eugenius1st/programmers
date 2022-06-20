def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part #해시값으로 dictionary에 저장
        temp += int(hash(part))

    for com in completion:
        temp -= hash(com)
    answer = dic[temp] # 특정 해시값으로 dictionary 조회

    return answer