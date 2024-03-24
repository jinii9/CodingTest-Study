arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)): # 가림막
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반목하는 문법
        if arr[j] < arr[j-1]: # 1칸씩 왼쪽으로 이동
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            # -> 정렬이 이루어진 원소는 항상 오름차순을 유지하고 있으므로 자기보다 작은 데이터를 만났다면 더 이상 데이터 살펴볼 필요 X
            break

print(arr)