# 40분~
# 4
# 1 3 1 5
# 짝수 or 홀수

n = int(input())
k = list(map(int, input().split())) # 식량 개수

# d = [0] * 10000001
d = [0] * 100
# d의 인덱스 : k의 인덱스 or
# d의 인덱스 값 : 식량의 최댓값

d[0] = k[0]
d[1] = k[1]
for i in range(2, n+1):
    d[i] = max(d[i], d[i-2], d[i] + d[i-2])

print(d[n])
print(d[n+1])
