# time : 15분
# 5
# 8 3 7 9 2
# 3
# 5 7 9
def binary_search(arr, target, start, end):
    # print(arr, target, start, end)
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

# 입력
n = int(input())
item_data = list(map(int, input().split()))
item_data.sort()
m = int(input())
ask_data = list(map(int, input().split()))

for i in range(m):
    result = binary_search(item_data, ask_data[i], 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

