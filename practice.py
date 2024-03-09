# input
# 4 6
# 19 15 10 17
n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total += (i - mid)

        if total >= target: # 많이 잘랐기 때문에 -> 오른쪽 이진탐색
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


result = binary_search(arr, m, 0, max(arr))
print(result)