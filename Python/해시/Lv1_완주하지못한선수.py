def solution(part, comp):
    marathon = {}
    for i in comp:
        marathon[i] = marathon.get(i,0) + 1

    for j in part:
        marathon[j] = marathon.get(j,0) -1
        print(marathon[j])
        if marathon[j] < 0:
            return j
        
