n, m = list(map(int, input().split())) # n: 강의 수, m: 블루레이 수
arr = list(map(int, input().split()))

def is_possible(bluray_size):
    count = 1 # 블루레이 개수
    total = 0 # 강의 시간 합계
    for i in range(n):
        if arr[i] > bluray_size:
            return False
        if total + arr[i] > bluray_size:
            count += 1
            total = 0
        total += arr[i]
    return count <= m



# binary_search(arr, target, start, end)
start, end = max(arr), sum(arr)
result = end

while start <= end:
    mid = (start + end) // 2 # 블루레이 크기
    if is_possible(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)