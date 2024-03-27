# 50~
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 60 60 100
# kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90
n = int(input())
data = []
for _ in range(n):
    # 이름, 국어, 영어, 수학
    name, a, b, c = input().split()
    data.append((name, int(a), int(b), int(c)))

print(data)

sorted_data = sorted(data, key=lambda s: (-s[1], s[2], -s[3], s[0]))

for i in sorted_data:
    print(i[0])

###########################################
# 처음에는 문제를 잘못 보고 모두 내림차순으로 생각하고, '선택 정렬'을 이용하여 풀었다.
# 그러나 sort 함수의 특징을 잘 알면, 정말 쉬워진다. => 튜플 중에서 1번째 원소의 순서에 맞게 정렬될 때, 1번째 원소의 값이 같은 경우 2번째 원소의 순서에 맞게 정렬...

# [개선]
# 입력할 때는, 그냥 string으로 받고, 이후에 정렬할 때 int로 바꿔주는 방법
## data.append(input().split())
## sorted_data.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 선택 정렬
# for i in range(n):
#     min_index = i
#     for j in range(i+1, n):
#         if data[min_index][1] > data[j][1]: # 1번
#             min_index = j
#         elif data[min_index][1] == data[j][1]: # 2번
#             if data[min_index][2] > data[j][2]:
#                 min_index = j
#             elif data[min_index][2] == data[j][2]: # 3번
#                 if data[min_index][3] > data[j][3]:
#                     min_index = j
#                 elif data[min_index][3] == data[j][3]: # 4번
#                     if data[min_index][0] > data[j][0]:
#                         min_index = j
#
#     data[i], data[min_index] = data[min_index], data[i]
#
# for i in range(n):
#     print(data[i][0])




