# 19~6
# 수확한 귤 중 k개를 골라 판매
# 귤을 크기별로 분류, 서로 다른 종류의 수 최소화

# 귤 8개, 1 3 2 5 4 5 2 3
# 귤 6개, 1 4 제외 / 3 2 5 5 2 3 -> 총 3가지

# k  귤 고르는 숫자
# 최종 값 : 서로 다른 종류의 수 최솟값

# !귤의 크기라는 것 잊지 말 것!

# 6 / 3
## 1 2 2 3 3 4 5 5
## 2 2 3 3 5 5

# 4 / 1 3 2 5 4 5 2 3 -> 2
## 1 2 2 3 3 4 5 5
## 2 2 3 3

# 2 / 1
## 1 1 1 1 2 2 2 3
## 1

# 1. 정렬
# 2. '크기'가 같은 것끼리 묶는다?
# 2. 묶은 것 중에서 숫자가 많은 순으로 정렬
# 3. 숫자의 종류 순 카운트

def solution(k, tangerine):
    answer = 0
    count = 1
    countArr = []

    # 1. 귤 정렬
    tangerine.sort()
    
    # 2. 귤의 종류별 개수를 세기
    for i in range(len(tangerine)):
        if i == len(tangerine) - 1:
            countArr.append(count)
        else:
            if tangerine[i] == tangerine[i+1]:
                count += 1
            else:
                countArr.append(count)
                count = 1
    
    # 3. 귤 종류별 개수를 내림차순으로 정렬
    countArr.sort(reverse=True)
    # print(countArr)
    
    # 4. k개 이상의 귤을 얻기 위한 최소 귤 종류 수를 구하기
    sum_count = 0
    count2 = 0 # 현재까지 선택한 귤 종류의 수를 세는 변수
    for i in countArr:
        if k <= sum_count:
            # answer = count2
            break
        else: 
            sum_count += i
            count2 += 1
    
    answer = count2 # answer를 for문 밖에서 값을 지정해줄 것!
    return answer
#######################################
# 왜 그런지는 사실 모르겠지만, answer=count2를 for문 안에다가 적으면, 오답으로 나온다.

# 사실 count2 없이 문제 풀이가 가능하다.
# sum_count = 0
# for i in countArr:
#     sum_count += i
#     answer += 1
#     if k <= sum_count:
#         break

# return answer
