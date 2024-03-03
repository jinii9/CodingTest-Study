arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right: # 엇갈리지 않을 때까지
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr, 0, len(arr)-1)
print(arr)

##########################################################
# Q) 원소가 1개인 경우 'start==end' 사용하지 않는 이유
# A) 재귀 호출 과정에서 end가 start보다 작아질 수 있는 상황 대비 위함
## 'start == end'를 사용하면 원소가 하나인 경우를 처리
## 'start >= end'를 사용하면 원소가 하나인 경우와 더불어 분할이 불가능한 경우까지 모두 처리 가능 => 더 안전한 조건

# Q) 엇갈릴 때 'left>=right' 사용하지 않는 경우
# A) arr=[5,3,7,6] 예시일 경우, left와 right가 같을 때 분할 작업을 마치게 되는 문제 발생

# Q) 엇갈리지 않을 때까지의 경우 'left < right' 사용하지 않는 이유
# A) (교차하는 경우) left와 right가 같은 위치를 가리키는 경우를 처리 못함.