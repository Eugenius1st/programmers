# def solution(numbers):
#     ch = [0]*(10)
#     answer = 0
#     for i in numbers:
#         ch[i] = 1

#     for x in range(len(ch)):
#         if ch[x] == 0:
#             answer += x
#     return answer
def solution(numbers):
    return 45 - sum(numbers)
    # 두줄만에 끝낼 수 있단다..