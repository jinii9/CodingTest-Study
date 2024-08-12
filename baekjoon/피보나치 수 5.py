# 1. 반복문 : for문 이용 -> O(n)
n = int(input())

arr = [-1] * (n + 2) 
# (n+2)까지 만들어주는 이유 : n=0일 경우, fibo[0]까지만 접근 가능한데 우리는 초기값을 2개를 항상 설정해주고 있기 때문에
arr[0] = 0
arr[1] = 1

for i in range(2, n + 1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[n])

# 2. 재귀함수 & 메모이제이션 사용X : 재귀함수를 한번 돌 때 2번 호출 -> O(2^n)
# 똑같은 값을 여러번 계산
def fibo(x):
    # base case
    if x== 0:
        return 0
    elif x == 1:
        return 1
    # recursive case
    return fibo(x-1) + fibo(x-2)

n = int(input())
print(fibo(n))

# 3. 재귀함수 & 메모이제이션 사용O : O(n)
# 중복된 계산을 하지 않는다.
def fibo(x):
	global arr

	if arr[x] != -1:
		return arr[x]

	arr[x] = fibo(x - 1) + fibo(x - 2)
	return arr[x]


n = int(input())

arr = [-1] * (n + 2)
arr[0] = 0
arr[1] = 1

print(fibo(n))