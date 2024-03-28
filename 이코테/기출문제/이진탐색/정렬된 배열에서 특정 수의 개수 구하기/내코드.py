# 계수정렬로 해도 될거같은데, 시간 초과 판정 우려됨.

n, x = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search_1(arr, target, start, end): # 첫번째 target 위치
    while start <= end:
        mid = (start + end) // 2

        if (mid == 0 or target > arr[mid - 1]) and target == arr[mid]: # 첫번째 target 위치 판별 조건
            return mid
        elif target <= arr[mid]: # '같은 경우'도 왼쪽을 확인할 수 있도록 해줘야 함!
            end = mid - 1
        else:
            start = mid + 1
    return None

def binary_search_2(arr, target, start, end): # 두번째 target 위치
    while start <= end:
        mid = (start + end) // 2

        if (mid == len(arr) - 1 or target < arr[mid + 1]) and target == arr[mid]: # 마지막 target 위치 판별 조건
            return mid

        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return None

first = binary_search_1(arr, x, 0, n - 1)
last = binary_search_2(arr, x, 0, n - 1)
print(first, last)

if first == None or last == None:
    print(-1)
else:
    result = last - first + 1
    print(result)

#################################################
# [오답]
# 처음에는 target을 찾으면 pop을 해서 배열에서 제거하면서 count를 했다.
# 그러나 배열을 수정하는 것은 바이너리 서치 효율성을 낮추고, pop 연산 자체가 O(N) 시간 복잡도를 가지므로 전체 알고리즘의 효율성을 크게 저하시킴

# [풀이]
# '처음 등장하는 인덱스'와 '마지막으로 등장하는 인덱스'를 각각 계산 -> 인덱스끼리 빼기
## 첫번째 위치 판별 조건
### target > arr[mid - 1] : 현재 위치(mid)의 직전 요소는 target보다 작고, 현재 위치의 요소가 target과 일치한다면, 현재 위치는 target이 처음으로 나타나는 위치



# [첫번째 잘못된 풀이 코드]

# def binary_search(arr, target, start, end):
#     result = 0
#     while start <= end:
#         mid = (start + end) // 2
#
#         if target == arr[mid]:
#             result += 1
#             arr.pop(mid)
#             end -= 1
#             # return mid
#
#         elif target < arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     # print(result)
#     # return -1
#     return result
#
# result = binary_search(arr, x, 0, n - 1)
# if result == 0:
#     print(-1)
# else:
#     print(result)