#스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
# clothes의 각 행은 [의상의 이름, 의상의 종류]
def solution(clothes):
    answer = 1
    classify = dict()
    for a,b in clothes:
        if b in classify:   
            classify[b].append(a)
        else:
            classify[b] = [a]

    for a in classify:
        print(a)
        answer *= (len(classify[a])+1) # 이 친구는 변태라 선글라스 끼고 아무것도 안 입을 수 있으므로 +1

    return answer-1 # 옷을 아예 안입는 경우를 빼준다.