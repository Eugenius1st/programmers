from collections import deque 

def solution(prices):
    answer = []
    prices= deque(prices)
    while prices:
        cnt = 0
        tmp = prices.popleft()
        for x in prices:
            cnt += 1
            if tmp > x:
                break
        answer.append(cnt)
    return answer