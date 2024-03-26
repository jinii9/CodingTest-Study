# ~10
# 123402
# 7755

# n = int(input())
arr = list(map(int, input()))

sum1 = 0
sum2 = 0
for i in range(len(arr)):
    if i >= len(arr)//2:
        sum2 += arr[i]
    else:
        sum1 += arr[i]

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")

#####################################
# 답 비교
## 1. 입력 방법
### n = input()
### summary += int(n[i])

## 2. 로직
### i: sum1과 sum2를 각각 명시해서, for문 안에 f문으로 처리
### sol: summary 변수를 하나만 선언해서, for문 2개 사용 -> 왼쪽 부분의 자릿수의 합을 구할 때는 summary '더하기', 오른쪽 부분의 자릿수의 합을 구할 때는 summary '빼기'
#### 이후 summary가 0이라면, 동일하다고 판단



