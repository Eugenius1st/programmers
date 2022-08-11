def solution(s):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    checkN = ""
    answer = ""

    for ch in s:
        if ch.isdecimal(): #숫자일 경우
            answer+=ch
        else:
            checkN += ch
            if checkN in number: # append 된 checkN이 number안에 있을 경우
                answer += str(number.index(checkN))
                checkN = ""
    return int(answer)

# 멋진 코드
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)