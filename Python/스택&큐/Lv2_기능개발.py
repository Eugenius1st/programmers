def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1 #time이 누적되어 stack 값에 time을 곱해서 100이 넘으면 쫙쫙쫙 pop으로 빠짐.. 
            # 그리고 계속 time은 누적된다.
    answer.append(count)
    return answer