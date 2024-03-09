n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

## 현재 크기가 모든 강의를 담기에 충분한지를 판단하는 함수
def is_possible(bluray_size):
    count = 1  # 블루레이 개수
    total = 0  # 현재 블루레이에 담긴 강의 시간의 합
    for i in range(n): ## 각 강의 순회
        if arr[i] > bluray_size: ## arr[i] : 현재 강의
            return False  # 현재 강의 하나가 블루레이 크기보다 크면 불가능

        if total + arr[i] > bluray_size: ## 현재 강의를 현재 블루레이에 담았을 때 블루레이 크기를 초과하는지 확인
            count += 1  # 새로운 블루레이로 갈아타야 함!
            total = 0 ## 새 블루레이에 담긴 강의 시간 합계를 다시 계산하기 시작

        total += arr[i]
    return count <= m  # 블루레이 개수가 m 이하인지 확인

# 이진 탐색 시작과 끝 지정
start, end = max(arr), sum(arr)
result = end

while start <= end:
    mid = (start + end) // 2
    if is_possible(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
