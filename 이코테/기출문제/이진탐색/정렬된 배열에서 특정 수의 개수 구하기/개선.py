from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

def count_by_range(arr, left_value, right_value):
    left_idx = bisect_left(arr, left_value)
    right_idx = bisect_right(arr, right_value)
    print(left_idx)
    return right_idx - left_idx


count = count_by_range(arr, x, x)

if count == 0:
    print(-1)
else:
    print(count)

# 정렬된 상태에서 어디에 삽입할건지 인덱스를 찾아주는 것이므로
## 7 2
## 1 1 3 3 3 3 4
### 다음과 같이 입력하면, left_idx는 인덱스 2가 나온다.