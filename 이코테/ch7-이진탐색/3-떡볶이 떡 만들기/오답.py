# input
# 4 6
# 19 15 10 17
n,m = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()
k = arr[n-1] - arr[0]
print(k)

data = []
for i in range(k+1):
    data.append(arr[0] + i)
print(data)

def binary_search(arr, data, target, start, end):
    print(arr, data, target, start, end)

    # target 값
    count = 0
    for i in arr:
        count += data[i]

    if start > end:
        return 0
    mid = (start + end) // 2


result = binary_search(arr, data, m, 0, len(data)-1)

###########################################
# [오답] - 잘못된 생각
# 시작점과 끝점을 떡의 개별 높이 배열의 min, max로 잡았다.
# -> 당연히, 절단기의 높이 H는 0부터 가장 긴 떡의 길이 안에 있어야만 떡을 자를 수 있다!
## -> 생각해보면 start, end 값을 알면, data 배열을 따로 만들지 않아도 된다!
## 오답이지만 내 코드에서도 start와 end 값은 있다. 그러므로 start~end 값이 모두 들어가 있는 배열(data)을 만들지 않아도 된다.

# mid 값이 '잘랐을 때의 떡의 양을 계산한 값'보다 작거나 클 때 왼쪽, 오른쪽 부분 탐색 결정
# => 맞긴 했지만, mid 값이 전단기 높이 H라고 생각하지 못함!
# 이진 탐색으로 절단기의 높이 H를 바꾸면서 해야한다.(mid 값을 전단기 높이 H로!)

