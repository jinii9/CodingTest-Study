# 15분~
n = int(input())
input_data = []

for i in range(n):
    input_data.append(int(input()))

result = sorted(input_data, reverse=True)

for i in result:
    print(i, end=' ')

# 3
# 15
# 27
# 12

#########################################################
# [오답]
# for i in range(n):
#     input_data = list(map(int, input().split()))
# -> input_data를 계속 덮어쓰는중. 이전 입력 데이터 모두 사라지게 됨.
