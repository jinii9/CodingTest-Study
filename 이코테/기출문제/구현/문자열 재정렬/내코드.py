# 1. 문자열 / 숫자 분리
# 2. 문자열 오름차순
# 3. 숫자 더하기
# 4. 문자열 + 숫자 합치기

# K1KA5CB7
S = input()
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
text = ''
numSum = 0

for x in S:
    # 숫자이면 더하기
    if x in num:
        numSum += int(x)
    # 문자이면 오름차순
    else:
        text += x
    

text = ''.join(sorted(text))
# 숫자가 존재할 경우에만 문자열에 숫자 붙이기
if numSum != 0:
    answer = text + str(numSum)
    
print(answer)

####################################
# 문법(문자열인지 알 수 있는 문법)을 모르더라도 위와 같이 내가 할 수 있는 선에서 노력하면 문제를 풀 수 있다!
