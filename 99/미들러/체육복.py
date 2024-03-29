# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
# 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve

# 2, 4
# 1, 3, 5 -> 1,2 3or5,4 => 5
## 2번 앞뒤 확인 - 1,3
## 4번 앞뒤 확인 - 3,5
### 1번 앞뒤 확인 - 2 뒤
### 3번 앞뒤 확인 - 2,4 뒤
### 5번 앞뒤 확인 - 4,6

# 2, 4
# 3 -> 2or4 => 4
## 3번 앞뒤 확인 - 2,4

# 3
# 1 => 2
# 1번 앞뒤 확인 - 2

# 4	[2, 3]	[3, 4]	3
def solution(n, lost, reserve):
    lost.sort()  # 2 3
    reserve.sort()  # 3 4

    # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
    lost2 = []
    reserve2 = []
    for i in reserve:
        if i not in lost:  # i가 lost 리스트에 있는지 확인
            reserve2.append(i)
    for i in lost:
        if i not in reserve:
            lost2.append(i)

    answer = n - len(lost2)

    for i in reserve2:  # 3 4 / 1 3 5
        front = i - 1
        back = i + 1

        if front in lost2:
            lost2.remove(front)
            answer += 1

        elif back in lost2:
            lost2.remove(back)
            answer += 1

    print(answer)
    return answer

# 처음에는 이중 for문을 써서 하려다보니까 pop()을 쓰고 싶어도 range에러가 날까봐 배열에서 제거하지 못했었다.
# 그러다보니 이중 for문 안에서 reserve와 lost에 같은 숫자가 있어서 제거해줘도, 이미 전 for문을 돌 때 (전이기 떄문에)제거되지 못한 lost가 사용될 수 있기 때문에 틀리게 되어 버리는 것!
# 따라서 초반에 제거를 해주고 들어가야 한다....!
# [문법]
# not in, in 문법
# pop() 메서드는 인덱스를 기반으로 요소를 제거하며, 제거된 요소를 반환
# 반면, remove() 메서드는 특정 값을 찾아 제거하고, 값을 반환하지 X





# def solution(n, lost, reserve):
#     lost.sort()
#     reserve.sort()
#
#     answer = n - len(lost)  # 3
#
#     for i in range(len(reserve)):  # 1, 3, 5
#         front = reserve[i] - 1
#         back = reserve[i] + 1
#
#         for j in range(len(lost)):  # 2, 4
#             if reserve[i] == lost[j]:  # reserve에 있는 학생도 도난 당할 시,
#                 reserve[i] = -10
#                 answer += 1
#                 break
#             if front == lost[j]:
#                 lost[j] = -10
#                 answer += 1
#                 break
#             elif back == lost[j]:
#                 lost[j] = -10
#                 answer += 1
#
#     print(answer)
#     return answer


