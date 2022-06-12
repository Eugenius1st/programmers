def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    lst = {}
    check = {}
    
    for s in report:
        a, b = s.split(' ') 
        
        if b not in check:
            check[b] = 1
        else:
            check[b] += 1
            
        if a not in lst:
            lst[a] = [b]
        else:
            if b not in lst[a]:
                lst[a] += [b]

    for id_, n  in check.items():
        if n >= k:
            for user, user2 in lst.items():
                if id_ in user2:
                    answer[id_list.index(user)] += 1

    return answer