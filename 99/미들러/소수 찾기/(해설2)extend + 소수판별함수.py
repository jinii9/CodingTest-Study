from itertools import permutations


# 013
# 0 1 3
# 01 13 10 31
# 013 130 ...


# 소수 판별 함수
def isPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False  # 소수 아님

    return True


def solution(numbers):
    answer = 0
    prime = []
    # 1. 모든 숫자 조합
    for i in range(len(numbers)):
        prime.extend((list(map(int, map("".join, permutations(list(numbers), i + 1))))))

    # 2. 소수 판별
    for i in set(prime):
        if isPrime(i):
            print(i)
            answer += 1

    print(answer)
    return answer