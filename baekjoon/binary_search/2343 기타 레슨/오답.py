# n: 강의 수, m: 블루레이 수
# 블루레이 크기 최소로. 모두 같은 크기

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

# def binary_search(arr, target, start, end):
start = 0
end = sum(arr)

result = 0
while start <= end:
    mid = (start + end) // 2 # 블루레이 크기
    total = 0
    for i in range(len(arr)):
        while total < mid:
            total += arr[i]

    if total > mid:
        start = mid + 1
    else:
        result = mid
        end = mid - 1

print(result)

######################################################
# [오답] 이유
## 1. start 값은 0이 아니라 max(arr)이다!
## 2. 주어진 블루레이 크기(blulay_size)를 기반으로 모든 강의를 m개(블루레이 개수)의 블루레이에 나눠 담을 수 있는지 검사하는 함수를 구현하지 못했다.
