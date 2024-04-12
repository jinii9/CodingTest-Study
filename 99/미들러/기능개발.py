## 35
# progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌
# speeds : 개발 속도

# 93, 1 -> 7일
# 30, 30 -> 3일
# 첫번째 기능이 아직 완성된 상태가 아니기 때문에 7일째 배포
# 55, 5 -> 9일
# => 7일 2개, 9일 1개

## 5, 10, 1, 1, 20, 1
### 1 3 2

# 로직
# 1. 100-93 = 7 -> 7//1 = 7일
# 2. 100-30 = 70 -> 70//30 = 2 + 나머지 값
# 3. 100-55 = 45 -> 45//5 == 9일
# 1. > 2. 배포 2개
# 1. < 2. 배포 1개,
#
## 7 2 9
def solution(progresses, speeds):
    answer = []
    builds = []
    # 배포 날짜 구하기
    for i, pro in enumerate(progresses):
        left = 100 - pro  # 60
        # build = (left // speeds[i]) + (left % speeds[i])
        build = (left // speeds[i])

        if left % speeds[i] != 0:
            build += 1

        builds.append(build)

    #  각 배포마다 몇 개의 기능이 배포되는지 구하기
    day = builds[0]  # 7
    result = 0
    for i, build in enumerate(builds):
        if day >= build:
            result += 1
        elif day < build:
            answer.append(result)  # 이전 값 answer 배열에 추가하고,
            day = build # 배포 날짜 업그레이드
            result = 1

        if i == len(builds) - 1:  # 마지막 값 처리해주기!!
            answer.append(result)

    return answer

