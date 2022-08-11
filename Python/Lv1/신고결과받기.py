def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    lst = {}
    check = {}
    
    for s in report:
        a, b = s.split(' ') #신고 한 유저, 신고당한 유저
        
        if b not in check:
            check[b] = 1
        else:
            check[b] += 1 #check는 b가 신고 당한 정도 count 
            
        if a not in lst:
            lst[a] = [b]
        else:
            if b not in lst[a]: #lst는 a가 신고한 유저 목록
                lst[a] += [b]

    for id_, n  in check.items(): #신고 count 조회
        if n >= k: # k보다 크거나 같은지 확인
            for user, user2 in lst.items(): # 신고유저 목록 조회
                if id_ in user2: # id_(k이상 신고당한 유저)가 있는지 lst라는 유저목록 리스트에서 확인
                    answer[id_list.index(user)] += 1 # user가 들어있는 index값을 찾아 +1 해준다

    return answer