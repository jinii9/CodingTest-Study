import itertools


# 10~
# 소수 판별 방법 : 1, 자기자신
# 2, 3, 5, 7, 9, 11 ...
#

from itertools import permutations
import math

def solution(n):
    prime = set()

    ### n : "011"

    # 1. 모든 숫자 조합을 만든다
    for i in range(len(n)):
        print(list(n))  # n의 string을 하나씩 자른다.
        ### n : ['0', '1', '1']

        # 주어진 문자열로부터 가능한 모든 순열을 생성하고, 이를 다시 문자열로 변환하여 보여줍니다.
        # 순열을 생성하는 과정에서 permutations 함수는 각 순열을 튜플 형태로 반환하며, map 함수를 사용하여 각 튜플을 문자열로 결합합니다.
        print(list(permutations(list(n), i + 1)))  ## list(n)으로 부터 i+1개짜리 순열을 만들어 tuple로 반환한다
        ## 순열이란 n개의 원소를 사용해서 순서를 정하여 r개의 배열로 나타내는 것을 말한다. 순열은 순서가 있기 때문에 원소의 종류가 같아도 순서가 다르면 다른배열이 된다.
        ### n : [('0',), ('1',), ('1',)]
        ### n : [('0', '1'), ('0', '1'), ('1', '0'), ('1', '1'), ('1', '0'), ('1', '1')]
        ### n : [('0', '1', '1'), ('0', '1', '1'), ('1', '0', '1'), ('1', '1', '0'), ('1', '0', '1'), ('1', '1', '0')]

        print(list(map("".join, permutations(list(n), i + 1))))  ## 각 튜플을 문자열로 결합
        ## map이란 반복가능한 객체에 각각 함수를 적용하고 싶을 때 사용하는 함수
        ### n : ['0', '1', '1']
        ### n : ['01', '01', '10', '11', '10', '11']
        ### n : ['011', '011', '101', '110', '101', '110']

        # 최종
        print(list(map(int, map("".join, permutations(list(n), i + 1)))))
        ### n : [0, 1, 1]
        ### n : [1, 1, 10, 11, 10, 11]
        ### n : [11, 11, 101, 110, 101, 110]

        prime |= set(map(int, map("".join, permutations(list(n), i + 1))))
        # set함수 사용 이유 : 112를 입력 받을 경우, 두 자리 순열로 11이 2번 생성될 수 있기 때문에
        # 합집합(|=)연산 사용 이유 :  각 단계에서 생성된 숫자들을 효율적으로 prime 집합에 추가하기 위해

    # 2. 소수가 아닌 수를 제외한다.
    prime -= set(range(0, 2))  # 0과 1을 제거(0과 1은 소수가 아니기 때문에 제외)
    ## range(0, 2)는 0부터 1까지의 수를 생성
    ## set(range(0, 2))는 {0, 1} 집합 생성
    ## prime 집합에서 {0, 1}을 제거

    for i in range(2, int(math.sqrt(max(prime))) + 1):  # 2부터 prime 집합의 최대값의 제곱근까지의 모든 수를 순회
        prime -= set(range(i * 2, max(prime) + 1, i))  # i의 배수를 prime 집합에서 제거
    ## range(i * 2, max(prime) + 1, i)는 i의 배수들을 생성
    ## set(range(i * 2, max(prime) + 1, i))는 i의 배수들로 이루어진 집합을 생성
    ## prime -= set(range(i * 2, max(prime) + 1, i))는 prime 집합에서 i의 배수를 제거

    return len(prime)






# def solution(numbers):
#     answer = []
#     # numArr = []
#     # 숫자 조합하기(순열)
#     for i in range(len(numbers)):
#         # print(i)
#         # numArr.append(int(numbers[i]))
#         print(list(numbers))
#
#     # permutations = list(itertools.permutations(numArr, len(numArr)))
#     # for i in range(len(numbers)):
#     #     permutations.append()
#     # print(permutations)
#
#     return answer

# [오답 풀이] - 블로그 참고
# 순열과 조합 문법의 차이점
# for문을 통해 permutaions를 해야하는 이유 :  모든 숫자 조합 만들기 위해서