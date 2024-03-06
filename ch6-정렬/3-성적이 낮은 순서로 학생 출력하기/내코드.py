n = int(input())

arr = []
for i in range(n):
    input_data = input().split() ## input_data 값 : ['홍길동', '95']
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    arr.append((input_data[0], int(input_data[1])))

## arr 값 : [('홍길동', 95), ('이순신', 77)]

# 키(Key)를 이용하여, 점수를 기준으로 정렬
result = sorted(arr, key=lambda student: student[1])

for student in result:
    print(student[0], end=' ')

# 2
# 홍길동 95
# 이순신 77