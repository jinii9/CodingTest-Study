# 입력
# 2 15
# 2
# 3

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

d = [10001] * (m + 1)
# 인덱스 : 금액
# 인덱스 해당 값 : 최소 화폐 개수

d[0] = 0
for i in range(n): # 화폐 단위
    for j in range(arr[i], m + 1):
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
