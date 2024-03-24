# input
# 4 6
# 19 15 10 17
n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    result = 0 # 최적의 절단 높이를 저장할 변수
    while start <= end:
        total = 0
        mid = (start + end) // 2
        # 잘랐을 때의 떡볶이 양 계산
        for i in arr:
            if mid < i:
                total += (i - mid)

        # 떡볶이 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if total < target:
            end = mid - 1
        # 떡볶이 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else:
            result = mid  #(중요!) 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1
    return result  # 조건을 만족하는 최대 mid 값을 반환

result = binary_search(arr, m, 0, max(arr))
print(result)

####################################################
# 다음과 같이 기본 코드처럼 안하는 이유
# if total == mid:
#     return mid
# -> total과 mid를 비교하는 것은 의미가 X. 대신, total이 목표한 떡의 양 target과 같거나 큰지를 확인해야 함.
# => 그래서 오른쪽 부분을 탐색할 때 result = mid 코드를 넣어준다!
