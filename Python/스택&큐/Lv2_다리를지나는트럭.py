def solution(bridge_length, weight, truck_weights):
    answer = 0
    passing = [0 for _ in range(bridge_length)] 

    while passing:
        answer += 1
        passing.pop(0)
        if truck_weights:    
            if sum(passing) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                passing.append(t)
            else:
                passing.append(0)
        print(passing)
    return answer