import heapq

def solution(scoville, K):
    answer = 0
    pop1 = 0
    pop2 = 0
    heapq.heapify(scoville)
    while scoville and scoville[0] < K:
        pop1 = heapq.heappop(scoville)
        pop2 = heapq.heappop(scoville)
        heapq.heappush(scoville, pop1+(pop2*2))
        answer += 1
        ## 히든케이스 !!, 만약 남은 힙의 길이가 1 일 경우 pop을 할 수 없다.
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer