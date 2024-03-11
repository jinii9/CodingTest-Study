# 34분
n = int(input())
arr = list(map(int, input().split()))
m = int(input()) # target

start, end = 0, max(arr)
result = end

while start <= end:
    mid = (start + end) // 2 # 상한액
    total = 0
    for i in arr:
        if i < mid:
            total += i
        else:
            total += mid

    if total <= m:
        result = mid
        start = mid + 1
    else: # total > m
        end = mid - 1

print(result)



