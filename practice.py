# cul step
def binary_sesarch(arr, num):
    cur = -1
    step = len(arr)
    
    while step != 0:
        while (cur + step < len(arr) and arr[cur + step] <= num):
            cur += step
        step //= 2

print(binary_search([1, 3, 3, 4, 5, 7, 9, 10, 11, 13, 13, 16], 10))