from itertools import permutations

def isPrime(num):
    for i in range(2,int(num/2)+1):
        if num%i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    visited = []

    for i in range(1,len(numbers)+1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            if num == 0 or num == 1 : continue
            if num in visited : continue

            visited.append(num)
            if isPrime(num):
                answer += 1
    return answer