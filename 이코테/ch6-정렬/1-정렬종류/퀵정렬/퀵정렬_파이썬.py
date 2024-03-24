array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) ## '+'연산자 이용해서 3개의 리스트 연결

print(quick_sort(array))

##########################################################
# Q) left_side에 피벗과 같은 값을 가진 원소들도 위치시키는 이유 (<= 이유)
# A) 피벗과 같은 값을 가진 원소들도 정렬 대상으로 취급해야지 최종 정렬 결과에 반영되기 때문에
## 따라서 피벗과 같은 값을 가진 원소들을 왼쪽 혹은 오른쪽 리스트에 반드시 포함시켜야하는데 일반적으로 왼쪽에 포함.

# Q) return 시, [pivot] 리스트 추가 이유 (left_side에 피벗)
# A) 피벗 자체는 left_side나 right_side에 포함되지 않아서, 재귀 호출에서는 더 이상 참조되지 않게 됨.
## 따라서, 각 부분을 별도로 정렬한 후에는 피벗 자체가 빠져있게 되므로, 이를 다시 추가해줘야 함!