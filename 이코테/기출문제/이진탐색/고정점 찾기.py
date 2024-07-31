# 45~
# 정렬되어 있다.
# O(logN) -> 이진탐색
# 고정점 : 그 값이 인덱스와 동일한 원소
# 고정점이 있다면 고정점 출력
# 고정점이 없다면 -1

# -15 -6 1 3 7
# 3

# target start mid end
def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2

        if mid == array[mid]:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1



n = int(input())
array = list(map(int, input().split()))
print(array)
print(binary_search(array, 0, n-1))

#################################
# '찾고자 하는 값'이 '중간점'과 동일하다고 가정한다.(->정렬이 되어있기 때문에 가능한 부분)

# 7
# -15 -4 2 8 9 13 15