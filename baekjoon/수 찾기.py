# N 자연수
# M 수들
# 배열 A 안에 존재하는지 확인

def binary_search(arr, num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < num:
            left = mid + 1

        if arr[mid] > num:
            right = mid - 1
        
        if arr[mid] == num:
            return True
    
    return False
        

# Marr이 Aarr 안에 있는지
N = int(input())
Aarr = sorted(list(map(int, input().split())))
M = int(input())
Marr = list(map(int, input().split()))

for m in Marr:
    if binary_search(Aarr, m): # 존재하면
        print("1")
    else: # 존재 X 하면
        print("0")

