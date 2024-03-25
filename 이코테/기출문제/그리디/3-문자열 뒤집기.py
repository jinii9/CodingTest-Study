# ~40
# 010011000000000
# 0001100

s = list(map(int, input()))

# 여기서 뽀인트는 0과 1의 그룹의 수를 파악하는 것!
zero_group = 0
one_group = 0
before = s[0]

# 문자열 첫 번쨰
if before == 0:
    zero_group = 1
else:
    one_group = 1

# 문자열 첫 번째 이외에
for i in range(1, len(s)):
    if before != s[i] and before == 0:
        zero_group += 1
    elif before != s[i] and before == 1:
        one_group += 1

    before = s[i]

# if zero_group < one_group:
#     print(zero_group)
# else:
#     print(one_group)
## -> 고치기
print(min(zero_group, one_group))

#############################################
# 파이썬에서 문자열은 배열(리스트)로 취급되기 때문에
## data=input()으로 받아도 -> data[0] 이런 식으로 접근 가능