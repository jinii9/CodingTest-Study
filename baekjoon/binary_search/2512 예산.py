# 34분
n = int(input())
arr = list(map(int, input().split()))
m = int(input()) # target

# binary_search(arr, target, start, end)
# start, end = max(arr), sum(arr)
start, end = 0, max(arr)
result = end

print(arr)
while start <= end:
    print("start, end:", start, end)
    mid = (start + end) // 2 # 상한액
    print("mid:", mid)
    total = 0
    for i in arr:
        if i < mid:
            total += i
        else:
            total += mid

    print("total:", total)

    if total <= m: # 현재 상한액(mid)으로 모든 지방의 예산요청 만족 가능 but 가능한 최대의 총예산을 배정하기 위해(더 큰 상한액을 찾기 위해)
        result = mid
        start = mid + 1
    else: # total > m -> 총 예산 초과
        end = mid - 1

print(result)

####################################################
# 처음에 잘못 생각한 포인트
## 처음에는 start, end = max(arr), sum(arr)이라고 지정했었다.
## mid는 '전체 국가예산'이 아니라 '상한액'이다.
## 조건문에서 어디를 mid와 같게 해야하는지 헷갈렸다. => 'total <= m'




