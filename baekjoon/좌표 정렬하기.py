# x좌표가 증가하는 순, 같다면 y좌표가 증가하는 순서 정렬

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

# arr = sorted(arr, key = lambda x: (x[0], x[1]))
arr = sorted(arr)

# for x in arr:
#     print(x[0], end=' ')
#     print(x[1])

for x, y in arr:
    print(x, y)