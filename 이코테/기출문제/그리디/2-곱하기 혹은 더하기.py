# ~15
# 02984
s = list(map(int, input()))

result = 0
for i in range(len(s)):
    if s[i] <= 1 or result <= 1:
        # print(result, end='')
        result += s[i]
        # print("+", s[i], "=", result)
    else:
        # print(result, end='')
        result *= s[i]
        # print("*", s[i], "=", result)

print(result)


#############################################
# 1인 경우에도 곱하기 말고 '더하기'로 수행해야 한다!

