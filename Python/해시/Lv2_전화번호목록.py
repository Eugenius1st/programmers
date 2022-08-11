def solution(phone_book):
    answer = True
    dic = {}
    # 해시 리스트를 만든다
    for p in phone_book:
        dic[p] = 1
    # 접두어가 Hash map에 존재하는지 찾는다
    for p in phone_book:
        tmp = ""
        for num in p:
            tmp += num
            if tmp in dic and tmp!=p:
                answer = False
    return answer
