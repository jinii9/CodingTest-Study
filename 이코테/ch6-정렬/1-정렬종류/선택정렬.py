arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i # 차례대로 타깃 선택
    for j in range(i+1, len(arr)): # 타깃보다 작은거 찾기
        if arr[min_index] > arr[j]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i] # 타깃과 작은거 스와프

print(arr)