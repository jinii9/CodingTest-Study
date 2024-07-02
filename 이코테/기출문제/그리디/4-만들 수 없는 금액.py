# n = 5
# 3 2 1 1 9
## 1 1 2 3 9
# 8

# n = 3
# 3 5 7
# 1
## 

# n = int(input())
# arr = list(map(int, input().split()))
n = 5
# arr = [3, 2, 1, 1, 9]
arr = [1, 2, 4]
arr.sort() # 1 1 2 3 9

cnt = 1
for x in arr:
    if cnt < x: # 만들 수 없는 금액을 찾았을 때 반복 종료
        break
    cnt += x

print(cnt)


#####################################
# (cnt = target)
# 핵심은 target 이하의 값은 모두 만들 수 있다고 정의하는 것
# 1. target 금액은 1부터 시작하고 화폐 단위는 오름차순으로 정렬한다.
# 2. 화폐 단위를 순차적으로 검사하면서 만약 target보다 단위가 작을 경우 해당 target은 만들 수 있다.
# 3. target을 만들 수 있을 경우, 다음 target은 해당 화폐 단위를 더한 값으로 갱신한다.
# 4. target보다 큰 값이 검사 단위로 주어질 경우 해당 target은 만들지 못한다고 판단하여 답으로 출력한다.



