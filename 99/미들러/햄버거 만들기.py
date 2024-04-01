def solution(ingredient):
    # 햄버거를 만드는데 필요한 순서
    burger_pattern = [1, 2, 3, 1]
    # 현재까지의 재료 순서를 저장할 스택
    stack = []
    # 포장한 햄버거의 개수
    burger_count = 0

    for i in ingredient:  # [2, 1, 1, 2, 3, 1, 2, 3, 1]
        # 현재 재료를 스택에 추가
        stack.append(i)
        # 스택의 길이가 햄버거 패턴의 길이보다 크거나 같고, 스택의 마지막 부분이 패턴과 일치하는지 확인
        print(stack[-len(burger_pattern):])
        if len(stack) >= len(burger_pattern) and stack[-len(burger_pattern):] == burger_pattern:
            # 패턴과 일치하면 포장한 햄버거의 개수를 증가시키고, 패턴에 해당하는 재료를 스택에서 제거
            burger_count += 1
            stack = stack[:-len(burger_pattern)]

        print("stack:", stack)

    return burger_count
solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
# 시간 초과 발생
# 1.리스트에서 요소를 제거(pop)하는 과정
## pop 연산은 리스트에서 요소를 제거할 때 해당 요소 뒤에 있는 모든 요소를 한 칸씩 앞으로 이동시켜야 하기 때문에 시간 복잡도가 O(n)
## 이 연산을 반복적으로 수행하면 전체 시간 복잡도가 매우 커질 수 있다.

# 2.패턴을 찾을 때마다 전체 리스트를 복사하고, ingredient 리스트를 temp로 업데이트
## 리스트의 복사 또한 시간 복잡도가 O(n)

# => 리스트에서 요소를 제거하는 대신 인덱스를 이용해 재료의 순서를 확인하고, 패턴을 찾으면 해당 햄버거를 포장한 것으로 간주한 후 다음 재료로 넘어가는 방식으로 로직을 개선

# def solution(ingredient):
#     answer = 0
#     count = 0
#     temp = list(ingredient)
#
#     i = 0
#     while i < len(ingredient):
#         if ingredient[i] == 1:
#             temp.pop(i)
#             if i < (len(ingredient) - 1) and ingredient[i + 1] == 2:
#                 temp.pop(i)
#                 if i < (len(ingredient) - 2) and ingredient[i + 2] == 3:
#                     temp.pop(i)
#                     if i < (len(ingredient) - 3) and ingredient[i + 3] == 1:
#                         temp.pop(i)
#                         count = 1
#                         answer += 1
#         if count == 1:
#             ingredient = list(temp)
#             count = 0
#             i = 0
#         else:
#             temp = list(ingredient)
#             i += 1
#
#     return answer

